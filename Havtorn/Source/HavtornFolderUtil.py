from enum import Enum
from enum import auto

GenerateProjectFilesPath = "./../ProjectSetup/GenerateProjectFiles.bat"

class HavtornFolders(Enum):
        Core = auto()
        Engine = auto()
        Editor = auto()
        Launcher = auto()
        Game = auto()
        Platform = auto()
        GUI = auto()
        Shaders = auto()
        PixelShaders = auto()
        VertexShaders = auto()
        GeometryShaders = auto()
        ShaderIncludes = auto()
        External = auto()
        ImGui = auto()
        ImGuizmo = auto()
        ImGuiNode = auto()

class HavtornFolderUtil:
    @staticmethod
    def get_folder_path(key:HavtornFolders):
        dictionary = {
                HavtornFolders.Core:"Core/",
                HavtornFolders.Engine:"Engine/",
                HavtornFolders.Editor:"Editor/",
                HavtornFolders.Launcher:"Launcher/",
                HavtornFolders.Game:"Game/",
                HavtornFolders.Platform:"Platform/",
                HavtornFolders.GUI:"GUI/",
                HavtornFolders.Shaders:"Engine/Graphics/Shaders/",
                HavtornFolders.PixelShaders:"Engine/Graphics/Shaders/",
                HavtornFolders.VertexShaders:"Engine/Graphics/Shaders/",
                HavtornFolders.GeometryShaders:"Engine/Graphics/Shaders/",
                HavtornFolders.ShaderIncludes:"Engine/Graphics/Shaders/Includes/",
                HavtornFolders.External:"../External/",
                HavtornFolders.ImGui:"../External/imgui/",
                HavtornFolders.ImGuizmo:"../External/ImGuizmo/",
                HavtornFolders.ImGuiNode:"../External/imgui-node-editor/",
        }
        try:
            return dictionary[key]
        except:
            print("No folder path for " + key.name)
            return ""
    
    @staticmethod
    def get_cmake_variable_name(key:HavtornFolders):
        dictionary = {
                HavtornFolders.Core:"set(CORE_FILES\n",
                HavtornFolders.Engine:"set(ENGINE_FILES\n",
                HavtornFolders.Editor:"set(EDITOR_FILES\n",
                HavtornFolders.Launcher:"set(LAUNCHER_FILES\n",
                HavtornFolders.Game:"set(GAME_FILES\n",
                HavtornFolders.Platform:"set(PLATFORM_FILES\n",
                HavtornFolders.GUI:"set(GUI_FILES\n",
                HavtornFolders.PixelShaders:"set(PIXEL_SHADERS\n",
                HavtornFolders.VertexShaders:"set(VERTEX_SHADERS\n",
                HavtornFolders.GeometryShaders:"set(GEOMETRY_SHADERS\n",
                HavtornFolders.ShaderIncludes:"set(SHADER_INCLUDES\n",
                HavtornFolders.ImGui:"set(IMGUI_FOLDER\n",
                HavtornFolders.ImGuizmo:"set(IMGUIZMO_FOLDER\n",
                HavtornFolders.ImGuiNode:"set(IMGUI_NODE_FOLDER\n",
        }
        try:
            return dictionary[key]
        except:
            print("No CMake variable name for " + key.name)
            return ""
    
    @staticmethod
    #TODO: what is the actual name for this?
    def get_file_specifier(key:HavtornFolders):
        dictionary = {
                HavtornFolders.PixelShaders:"_PS",
                HavtornFolders.VertexShaders:"_VS",
                HavtornFolders.GeometryShaders:"_GS",
        }
        try:
            return dictionary[key]
        except:
            print("No file specifier for " + key.name)
            return ""

if __name__ == "__main__":
    for folder in HavtornFolders:
        print(folder.name)
        
        path = HavtornFolderUtil.get_folder_path(folder)
        if path:
            print(" Path: " + repr(path))
        
        cmake = HavtornFolderUtil.get_cmake_variable_name(folder)
        if cmake:
            print(" CMake var: " + repr(cmake))

        fileSpec =  HavtornFolderUtil.get_file_specifier(folder)
        if fileSpec:
            print(" File spec: " + repr(fileSpec))
    
        print()
    input("Any key to continue ...")
