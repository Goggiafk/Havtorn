import os
import re
from enum import Enum
from glob import glob
from collections import defaultdict
from HavtornMainFoldersUtility import HavtornMainFoldersUtility
from HavtornMainFoldersUtility import HavtornKeys


# Scans Havtorn's Source-folder for files and adds them to CMakeLists
# External-folders are excluded from scan since we want a handpicked selection from them
class CMakeTextsGenerator:
    targets = {
        HavtornKeys.Core,
        HavtornKeys.Engine,
        HavtornKeys.Editor,
        HavtornKeys.Launcher,
        HavtornKeys.Platform,
        HavtornKeys.Game,
        HavtornKeys.GUI,
        HavtornKeys.PixelShaders,
        HavtornKeys.VertexShaders,
        HavtornKeys.GeometryShaders,
        HavtornKeys.ShaderIncludes,
    }

    targetSpecficNameFilters = {
        HavtornKeys.PixelShaders:{
            HavtornMainFoldersUtility.get_file_specifier( HavtornKeys.PixelShaders),
            },
        HavtornKeys.VertexShaders:{
            HavtornMainFoldersUtility.get_file_specifier( HavtornKeys.VertexShaders),
            },
        HavtornKeys.GeometryShaders:{
            HavtornMainFoldersUtility.get_file_specifier( HavtornKeys.GeometryShaders),
            },
    }
    # add .hint, .vcxproj.user,
    targetSpecificExclusions = {
        HavtornKeys.Engine:{
            'Shaders',
            },
    }

    exclusions = {
        ".hint",
        ".vcxproj.user",
    }

    # put in __init__
    filesToAdd = defaultdict(list[str])

    @classmethod
    def Test(self):
        for target in self.targets:
            self.filesToAdd.update({target : list[str]()})
            try:
                exclusions = '|'.join(self.exclusions)

                specificExclusions = ''
                if target in self.targetSpecificExclusions:
                    specificExclusions = '|'.join(self.targetSpecificExclusions[target])

                fileNameFilters = ''
                if target in self.targetSpecficNameFilters:
                    fileNameFilters = '|'.join(self.targetSpecficNameFilters[target])
                
                for file in glob(os.path.abspath(HavtornMainFoldersUtility.get_folder_path(target)) + '/**', recursive=True):
                    if not os.path.isfile(file):
                        continue
                    if (exclusions and re.search(exclusions, file)):
                        continue
                    if (specificExclusions and re.search(specificExclusions, file)):
                        continue
                    if (fileNameFilters and not re.search(fileNameFilters, file)):
                        continue
                    
                    toAdd = file.split("Source\\")[1]
                    toAdd = toAdd.replace("\\", "/")
                    self.filesToAdd[target].append(toAdd)
            except Exception as e:
                print(e)

        templatePath = "CMakeListsTemplate.txt"
        cmakeListsPath = "CMakeLists.txt"

        cmakeFileAsLineList = list[str]
        with open(templatePath, "r") as templateFile: 
            cmakeFileAsLineList = templateFile.readlines()
        
        for target in self.targets:
            cmakeFileTargetName = HavtornMainFoldersUtility.get_cmake_variable_name(target)
            for toAdd in self.filesToAdd[target]:
                cmakeFileAsLineList.insert(cmakeFileAsLineList.index(cmakeFileTargetName) + 1, "\t" + toAdd + "\n")

        with open(cmakeListsPath, "w") as cmakeFile:
            cmakeFile.flush()
            cmakeFile.writelines(cmakeFileAsLineList)
        return

    @classmethod
    def Do(self):
        # for all main folders
            # get all [cpp, h, ..etc] 
        for mainFolder in self.mainFolders:
            print(mainFolder)
            try:
                for file in glob(os.path.abspath(mainFolder) + '/**', recursive=True):
                    if os.path.isfile(file):
                        print("\t" + file.split("Source\\")[1])
            except Exception as e:
                print(e)

        print(self.externalFolder)
        try:
            for file in glob(os.path.abspath(self.externalFolder) + '/**', recursive=True):
                if os.path.isfile(file):
                    print("\t ..\\External\\ " + file.split("\\External\\")[1])
        except Exception as e:
            print(e)
            #for file in os.listdir(mainFolder):
            #    try:
            #        print("\t" + os.path.abspath(file) + "  " + f"{os.path.isfile(os.path.abspath(file))}")
            #    except Exception as e:
            #        print(e)

        while(True):
            c = input("c to close")
            if c == "c":
                break
        return

if __name__ == "__main__":
    generator = CMakeTextsGenerator()
    generator.Test()