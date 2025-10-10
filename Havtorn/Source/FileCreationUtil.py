import os
import subprocess
import re
import io
import time

from HavtornFolderUtil import HavtornFolderUtil
from HavtornFolderUtil import HavtornFolders
from ValidationUtils import ValidationUtil

# TODO: Look over if it is possible to restructure how CMakeLists and this script tracks directories -> Generate CMakeLists through script?

class FileCreationUtil:
    # class variables, should not be altered
    # TODO: If more filetypes are supported the characters used for the license comment need to be filtered, same goes for namespace structure
    havtornLicense="// Copyright 2025 Team Havtorn. All Rights Reserved.\n\n"
    havtornNameSpace="\nnamespace Havtorn\n{\n\n}\n"
    cmakeListFilePath="CMakeLists.txt"
    
    inputCharacters = ">> "

    generatorScriptPath = "./../ProjectSetup/GenerateProjectFiles.bat"
    
    mainFolderChoices={
        HavtornFolders.Core.name,
        HavtornFolders.Platform.name,
        HavtornFolders.GUI.name,
        HavtornFolders.ImGui.name,
        HavtornFolders.ImGuizmo.name,
        HavtornFolders.ImGuiNode.name,
        HavtornFolders.Engine.name,
        HavtornFolders.ShaderIncludes.name, #TODO: if shader category, check extension & category to see if fileSpecifier is missing, if not add it. I.e coolshader.hlsl in VertexShaders should have _VS => coolshader_VS.hlsl
        HavtornFolders.VertexShaders.name,
        HavtornFolders.GeometryShaders.name,
        HavtornFolders.PixelShaders.name,
        HavtornFolders.Game.name,
        HavtornFolders.Editor.name,
        HavtornFolders.Launcher.name,
    }
    # So we always show them in the same order
    mainFolderChoices=sorted(mainFolderChoices)

    addFileCommand = "-f"
    addFileSingle = "-sf"
    undoFileCommand = "-u"
    switchMainCommand = "-m"
    continueCommand = "-g"

    @classmethod
    def __init__(self):
        self.mainFolder:HavtornFolders
        self.filesToAdd = []
        return

    @classmethod
    def print_command_separator(self):
        print()
        return

    @classmethod
    def on_error(self, errorMessage:str):
        print(f'<!> {errorMessage}')
        time.sleep(1)
        return

    @classmethod
    def select_main_folder(self):
        self.print_command_separator()
        print("Pick a main folder:")
        for option in HavtornFolders:
            print("\t" + option.name)

        self.print_command_separator()
        while(True):
            inputChoice = input(self.inputCharacters)
            for key in HavtornFolders:
                if inputChoice.lower() not in key.name.lower():
                    continue
                self.mainFolder = key
                return
                
            self.on_error(f'invalid option "{inputChoice}"')
        return
    
    @classmethod
    def print_options(self):
        self.print_command_separator()
        print(f' {self.addFileCommand} to add folder & file, example: "F1/f2/ex.cpp"')
        print(f' Some file-extensions have associated files auto-generated, example: "ex.h" gets a "ex.cpp"')
        print(f' {self.addFileSingle} same as {self.addFileCommand} without auto-generation of associated file')
        print(f' {self.undoFileCommand} to undo, example: {self.undoFileCommand} 1')
        print(f' {self.switchMainCommand} to change main folder')
        print(f' {self.continueCommand} continue to file generation')
        return
    
    @classmethod
    def print_status(self):
        self.print_command_separator()
        print(f"Main folder: {HavtornFolderUtil.get_folder_path(self.mainFolder)}")
        print(f"Files:")
        for i, (_, file) in enumerate(self.filesToAdd):
            print(f'+ [{i + 1}] {file}')
        return
    
    @classmethod
    def try_add_associated_file(self, fileName:str, folderNames:list[str]):
        # based on file extension determine if an additional file should be added
        fileNameSplit = fileName.split('.')
        extension = fileNameSplit[1]
        associatedExtension = ""
        match extension:
            case "cpp":
                associatedExtension = "h"
            case "c":
                associatedExtension = "h"
            case "h":
                associatedExtension = "cpp"
            case "hpp":
                associatedExtension = "cpp"
            case _:
                return
                
        folders = "/".join(folderNames)
        self.filesToAdd.append((self.mainFolder, HavtornFolderUtil.get_folder_path(self.mainFolder) + folders + "/" + fileNameSplit[0] + "." + associatedExtension))
        return
    
    @classmethod
    def valid_folder(self, folderName:str):
        if ValidationUtil.validate_folder_name(folderName) is False:
            self.on_error(f'"{folderName}" contains invalid characters')
            return False     
        return True
    
    @classmethod
    def valid_file(self, fileName:str):
        filenameSplit = fileName.split('.')
        if ValidationUtil.validate_file_name(filenameSplit[0]) is False:
            self.on_error(f'"{fileName}" contains invalid characters')
            return False
        
        if (len(filenameSplit) == 1 # Missing extension
            or len(filenameSplit) > 2 # More than 1 extension
            or ValidationUtil.validate_file_extension(filenameSplit[1]) is False):
            self.on_error(f'unsupported extension in "{fileName}"')
            return False
        
        return True

    @classmethod
    def extract_folders_and_file(self, fullFile:str):
        folderNames = fullFile.split('/')
        fileName = folderNames[-1]
        folderNames.pop()
        return (folderNames, fileName)

    @classmethod
    def try_add_header_prefixes(self, fileName:str, fileStream:io.TextIOWrapper):
        extension = fileName.split('.')[1]
        checks = [
            extension.lower() in [
                'h', 
                'hpp', 
                ],
        ]
        if not all(checks):
            return
        
        fileStream.write("#pragma once\n")
        return
    
    @classmethod
    def try_include_header(self, fileName:str, fileStream:io.TextIOWrapper):
        fileNameSplit = fileName.split('.')
        checks = [
            fileNameSplit[1].lower() in [
                'c', 
                'cpp', 
                ],
        ]
        if not all(checks):
            return
        
        fileStream.write(f'#include "{fileNameSplit[0]}.h"\n')
        return
    
    @classmethod
    def try_add_namespace(self, fileName:str, fileStream:io.TextIOWrapper):
        # based on file extension determine if namespace can be added
        extension = fileName.split('.')[1]
        checks = [
            extension.lower() in [
                'cpp', 
                'c', 
                'h', 
                'hpp', 
                ],
        ]
        if not all(checks):
            return
        
        fileStream.write(self.havtornNameSpace)
        return

    @classmethod
    def generate_files(self):
        for (_, fileToAdd) in self.filesToAdd:
            (folderNames, fileName) = self.extract_folders_and_file(fileToAdd)
            folders = "/".join(folderNames)
            if not os.path.exists(folders):
                os.makedirs(folders)

            try:
                with open(fileToAdd, "x") as file:
                    file.write(self.havtornLicense)
                    self.try_add_header_prefixes(fileName, file)
                    self.try_include_header(fileName, file)
                    self.try_add_namespace(fileName, file)    
                    print(f'> File "{fileToAdd}" created')
            except FileExistsError:
                self.on_error(f'"{fileToAdd}" already exists')
        return

    @classmethod
    #TODO: add to cmake-template if new External file, otherwise, just run GenerateCMakeLists.py
    def add_file_to_cmake(self, mainFolder:HavtornFolders, fileToAdd:str):
        # Read CMakeLists into a list of lines, append entry and rewrite file
        cmakeTarget = HavtornFolderUtil.get_cmake_variable_name(mainFolder) 
        entry=f"\t{fileToAdd}\n"
        fileAsLineList=list[str]
        with open(self.cmakeListFilePath, "r") as cmakeFile: 
            fileAsLineList = cmakeFile.readlines()
            fileAsLineList.insert(fileAsLineList.index(cmakeTarget) + 1, entry)
            cmakeFile.flush()
        with open(self.cmakeListFilePath, "w") as cmakeFile:
            cmakeFile.writelines(fileAsLineList)
        return
        
    @classmethod
    def generate_and_flush(self):
        self.generate_files()
        for (mainFolder, fileToAdd) in self.filesToAdd:
            self.add_file_to_cmake(mainFolder, fileToAdd)
        print("\nRegenerating project ...")
        subprocess.call([os.path.abspath(self.generatorScriptPath), "nopause"])
        self.filesToAdd = []
        return

    @classmethod
    def try_add_file(self, fileToAdd:str):
        if fileToAdd == "":
            return False

        (folderNames, fileName) = self.extract_folders_and_file(fileToAdd)
        foldersValid = True
        for filePart in folderNames:
            if not self.valid_folder(filePart):
                foldersValid = False
        if not foldersValid:
            return False
        if not self.valid_file(fileName):
            return False
        
        pendingAddition = (self.mainFolder, HavtornFolderUtil.get_folder_path(self.mainFolder) + fileToAdd)                        
        if pendingAddition in self.filesToAdd:
            self.on_error(f"trying to add duplicate {fileToAdd}")
            return False
        self.filesToAdd.append(pendingAddition)
        return True

    @classmethod
    def process_commands(self):
        while(True):
            self.print_options()
            self.print_status()

            userInput=input(self.inputCharacters)

            if self.continueCommand in userInput:
                self.generate_and_flush()
                self.print_command_separator()
                break

            if self.addFileCommand in userInput: 
                fileToAdd = "".join(userInput.replace(f"{self.addFileCommand}", '').split())
                if not self.try_add_file(fileToAdd):
                    continue
                
                (folderNames, fileName) = self.extract_folders_and_file(fileToAdd)
                self.try_add_associated_file(fileName, folderNames)
                continue
            
            if self.addFileSingle in userInput: 
                fileToAdd = "".join(userInput.replace(f"{self.addFileSingle}", '').split())
                self.try_add_file(fileToAdd)
                continue
            
            # TODO: nice to have - handle multiple indices at once
            if self.undoFileCommand in userInput:
                filesToUndo = re.findall('[0-9]+', userInput)
                if len(filesToUndo) == 0:
                    continue
                undoFileIndex = int(filesToUndo[0]) - 1 # To the user we display them as index+1, meaning input 1 == index 0
                if (len(self.filesToAdd) == 0
                    or undoFileIndex >= len(self.filesToAdd)):
                    continue

                del self.filesToAdd[undoFileIndex]
                continue
            
            if self.switchMainCommand in userInput:
                self.select_main_folder()
                continue 
        return

if __name__ == "__main__":
    print("** File Creation Utility **")
    print("Instructions:")
    print(" 1 - Select a main folder (can be changed), any file added will be placed under it")
    print(" 2 - Add as many files as you want.")
    print(" 3 - Generate: generation updates CMakeLists and updates the project files")
    print(" Use arrow-key up to retrieve previous input")
    print()
    fileCreator = FileCreationUtil()
    while(True):
        fileCreator.select_main_folder()
        fileCreator.process_commands()