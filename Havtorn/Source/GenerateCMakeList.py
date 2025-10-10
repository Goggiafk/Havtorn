import os
import re
from glob import glob
from collections import defaultdict

from HavtornFolderUtil import HavtornFolderUtil
from HavtornFolderUtil import HavtornFolders

# Scans Havtorn's Source-folder for files and adds them to CMakeLists
# External-folders are excluded from scan since we want a handpicked selection from them
class CMakeTextsGenerator:
    targets = {
        HavtornFolders.Core,
        HavtornFolders.Engine,
        HavtornFolders.Editor,
        HavtornFolders.Launcher,
        HavtornFolders.Platform,
        HavtornFolders.Game,
        HavtornFolders.GUI,
        HavtornFolders.PixelShaders,
        HavtornFolders.VertexShaders,
        HavtornFolders.GeometryShaders,
        HavtornFolders.ShaderIncludes,
    }

    targetSpecficNameFilters = {
        HavtornFolders.PixelShaders:{
            HavtornFolderUtil.get_file_specifier( HavtornFolders.PixelShaders),
            },
        HavtornFolders.VertexShaders:{
            HavtornFolderUtil.get_file_specifier( HavtornFolders.VertexShaders),
            },
        HavtornFolders.GeometryShaders:{
            HavtornFolderUtil.get_file_specifier( HavtornFolders.GeometryShaders),
            },
    }

    targetSpecificExclusions = {
        HavtornFolders.Engine:{
            'Shaders',
            },
    }

    exclusions = {
        ".hint",
        ".vcxproj.user",
    }

    @classmethod
    def __init__(self):
        self.filesToAdd = defaultdict(list[str])
        return
    
    # should also set the values of CMakes set under FOLDERS using HavtornFolders-values
    @classmethod
    def Run(self, templatePath:str, cmakeListsPath:str):
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
                
                for file in glob(os.path.abspath(HavtornFolderUtil.get_folder_path(target)) + '/**', recursive=True):
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

        cmakeFileAsLineList = list[str]
        with open(templatePath, "r") as templateFile: 
            cmakeFileAsLineList = templateFile.readlines()
        
        for target in self.targets:
            cmakeFileTargetName = HavtornFolderUtil.get_cmake_variable_name(target)
            for toAdd in self.filesToAdd[target]:
                cmakeFileAsLineList.insert(cmakeFileAsLineList.index(cmakeFileTargetName) + 1, "\t" + toAdd + "\n")

        with open(cmakeListsPath, "w") as cmakeFile:
            cmakeFile.flush()
            cmakeFile.writelines(cmakeFileAsLineList)
        return

if __name__ == "__main__":
    generator = CMakeTextsGenerator()
    generator.Run("CMakeListsTemplate.txt", "CMakeLists.txt")
