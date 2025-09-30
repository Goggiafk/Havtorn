import os
from glob import glob

class CMakeTextsGenerator:
    mainFolders = {
        "Core/",
        "Editor/",
        "Engine/",
        "Game/",
        "Launcher/",
        "GUI/",
        "Platform/",
        #External, Imgui, ...etc
        # everything under External/rapidjson/include
    }

    externalFolder = "../External/"

    # do special file filter for e.g Imgui:
    # imgui.cpp, imgui.h, imgui_tables.cpp, etc copy the ones currently used in CMakeList.txt

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
    generator.Do()