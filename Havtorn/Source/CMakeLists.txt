cmake_minimum_required (VERSION 3.31)

project (Havtorn
  DESCRIPTION "Havtorn"
  LANGUAGES CXX
  VERSION 1.0.0
)

# option(BUILD_TEST_TEMPLATE "Ignore warnings related to TODOs" OFF)

# option(ENABLE_CODE_ANALYSIS "Use Static Code Analysis on build" OFF)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

set(COMMON_COMPILE_DEFINITIONS HV_PLATFORM_WINDOWS HV_DEBUG HV_ENABLE_ASSERTS _UNICODE UNICODE)
set(COMMON_COMPILE_OPTIONS /W4 /WX /MP /ZI /JMC /fp:fast /FC)
set(COMMON_LINK_OPTIONS /WX /SUBSYSTEM:WINDOWS)

# ==================== FOLDERS ====================
set(ENGINE_FOLDER "Engine/")
set(SHADER_FOLDER "Engine/Graphics/Shaders/")
set(SHADER_INCL_FOLDER "Engine/Graphics/Shaders/Includes/")
set(EDITOR_FOLDER "Editor/")
set(GAME_FOLDER "Game/")
set(GUI_FOLDER "GUI/")
set(CORE_FOLDER "Core/")
set(PLATFORM_FOLDER "Platform/")
set(LAUNCHER_FOLDER "Launcher/")
set(EXTERNAL_FOLDER "../External/")
set(IMGUI_FOLDER "../External/imgui/")
set(IMGUIZMO_FOLDER "../External/ImGuizmo/")
set(IMGUI_NODE_FOLDER "../External/imgui-node-editor/")
set(RAPIDJSON_FOLDER "../External/rapidjson/include/rapidjson/")
set(WORKING_FOLDER "${CMAKE_BINARY_DIR}/../Bin/")
# ==================== FOLDERS ====================

# ==================== CORE ====================
set(CORE_FILES
	Core/Serializable.h
	Core/Serializable.cpp
	Core/MathTypes/Vector.h
	Core/MathTypes/Vector.cpp
	Core/MathTypes/Transform.h
	Core/MathTypes/Transform.cpp
	Core/MathTypes/Sphere.h
	Core/MathTypes/Rotator.h
	Core/MathTypes/Ray.h
	Core/MathTypes/Quaternion.h
	Core/MathTypes/Quaternion.cpp
	Core/MathTypes/PlaneVolume.h
	Core/MathTypes/Plane.h
	Core/MathTypes/Matrix3x3.h
	Core/MathTypes/Matrix.h
	Core/MathTypes/Matrix.cpp
	Core/MathTypes/MathUtilities.h
	Core/MathTypes/LineVolume.h
	Core/MathTypes/Line.h
	Core/MathTypes/Intersection.h
	Core/MathTypes/HavtornMath.h
	Core/MathTypes/Frustum.h
	Core/MathTypes/Frustum.cpp
	Core/MathTypes/EngineMathSSE.h
	Core/MathTypes/EngineMath.h
	Core/MathTypes/EngineMath.cpp
	Core/MathTypes/Curve.h
	Core/MathTypes/Curve.cpp
	Core/MathTypes/AABB3D.h
	Core/magic_enum.h
	Core/Log.h
	Core/Log.cpp
	Core/hvpch.h
	Core/hvpch.cpp
	Core/HavtornString.h
	Core/HavtornString.cpp
	Core/HavtornDelegate.h
	Core/GeneralUtilities.h
	Core/FileSystem.h
	Core/FileSystem.cpp
	Core/EngineTypes.h
	Core/EngineException.h
	Core/Delegate.h
	Core/Delegate.cpp
	Core/CoreTypes.h
	Core/Core.h
	Core/Color.h
	Core/Color.cpp
	Core/BitSet.h
)
set(RAPIDJSON_FILES
    "${RAPIDJSON_FOLDER}error/en.h"
    "${RAPIDJSON_FOLDER}error/error.h"
    "${RAPIDJSON_FOLDER}internal/biginteger.h"
    "${RAPIDJSON_FOLDER}internal/clzll.h"
    "${RAPIDJSON_FOLDER}internal/diyfp.h"
    "${RAPIDJSON_FOLDER}internal/dtoa.h"
    "${RAPIDJSON_FOLDER}internal/ieee754.h"
    "${RAPIDJSON_FOLDER}internal/itoa.h"
    "${RAPIDJSON_FOLDER}internal/meta.h"
    "${RAPIDJSON_FOLDER}internal/pow10.h"
    "${RAPIDJSON_FOLDER}internal/regex.h"
    "${RAPIDJSON_FOLDER}internal/stack.h"
    "${RAPIDJSON_FOLDER}internal/strfunc.h"
    "${RAPIDJSON_FOLDER}internal/strtod.h"
    "${RAPIDJSON_FOLDER}internal/swap.h"
    "${RAPIDJSON_FOLDER}msinttypes/inttypes.h"
    "${RAPIDJSON_FOLDER}msinttypes/stdint.h"
    "${RAPIDJSON_FOLDER}allocators.h"
    "${RAPIDJSON_FOLDER}cursorstreamwrapper.h"
    "${RAPIDJSON_FOLDER}document.h"
    "${RAPIDJSON_FOLDER}encodedstream.h"
    "${RAPIDJSON_FOLDER}encodings.h"
    "${RAPIDJSON_FOLDER}filereadstream.h"
    "${RAPIDJSON_FOLDER}filewritestream.h"
    "${RAPIDJSON_FOLDER}fwd.h"
    "${RAPIDJSON_FOLDER}istreamwrapper.h"
    "${RAPIDJSON_FOLDER}memorybuffer.h"
    "${RAPIDJSON_FOLDER}memorystream.h"
    "${RAPIDJSON_FOLDER}ostreamwrapper.h"
    "${RAPIDJSON_FOLDER}pointer.h"
    "${RAPIDJSON_FOLDER}prettywriter.h"
    "${RAPIDJSON_FOLDER}rapidjson.h"
    "${RAPIDJSON_FOLDER}reader.h"
    "${RAPIDJSON_FOLDER}schema.h"
    "${RAPIDJSON_FOLDER}stream.h"
    "${RAPIDJSON_FOLDER}stringbuffer.h"
    "${RAPIDJSON_FOLDER}uri.h"
    "${RAPIDJSON_FOLDER}writer.h"
)
add_library(Core SHARED ${CORE_FILES} ${RAPIDJSON_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${CORE_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR}"/../External/rapidjson/include" FILES ${RAPIDJSON_FILES})
target_include_directories(Core PRIVATE
    "${CORE_FOLDER}"
    "${EXTERNAL_FOLDER}rapidjson/include"
)
target_compile_definitions(Core PRIVATE ${COMMON_COMPILE_DEFINITIONS} HV_CORE_DLL)
target_compile_options(Core PRIVATE ${COMMON_COMPILE_OPTIONS})
target_link_options(Core PRIVATE ${COMMON_LINK_OPTIONS})
target_precompile_headers(Core PRIVATE ${CORE_FOLDER}hvpch.h)
set_property(TARGET Core PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_target_properties(Core PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
# ==================== CORE ====================

# ==================== PLATFORM ====================
set(PLATFORM_FILES
	Platform/WindowsInclude.h
	Platform/TestFileInPlatforn.cpp
	Platform/TestFileInPlatform.cpp
	Platform/PlatformProcess.h
	Platform/PlatformProcess.cpp
	Platform/PlatformManager.h
	Platform/PlatformManager.cpp
)
add_library(Platform SHARED ${PLATFORM_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${PLATFORM_FILES})
target_link_libraries(Platform PRIVATE
    Core
)
target_include_directories(Platform PRIVATE
	"${PLATFORM_FOLDER}"
    "${CORE_FOLDER}"
    "${EXTERNAL_FOLDER}rapidjson/include"
)
target_link_directories(Platform PRIVATE
    ${CMAKE_BINARY_DIR}
)
target_compile_definitions(Platform PRIVATE ${COMMON_COMPILE_DEFINITIONS} HV_PLATFORM_DLL)
target_compile_options(Platform PRIVATE ${COMMON_COMPILE_OPTIONS})
target_link_options(Platform PRIVATE ${COMMON_LINK_OPTIONS})
set_property(TARGET Platform PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_target_properties(Platform PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
add_dependencies(Platform Core)
# ==================== PLATFORM ====================

# ==================== GUI ====================
set(GUI_FILES
	GUI/GUIProcess.h
	GUI/GUIProcess.cpp
	GUI/GUI.h
	GUI/GUI.cpp
	GUI/FuzzySearch.h
	GUI/FuzzySearch.cpp
)
# We want a selection of files from ImGui & ImGui-related 
set(IMGUI_FILES
#  ------- SELECTION IMGUI -------
   ${IMGUI_FOLDER}imconfig.h
   ${IMGUI_FOLDER}imgui.cpp
   ${IMGUI_FOLDER}imgui.h
   ${IMGUI_FOLDER}imgui_demo.cpp
   ${IMGUI_FOLDER}imgui_draw.cpp
   ${IMGUI_FOLDER}imgui_internal.h
   ${IMGUI_FOLDER}imgui_tables.cpp
   ${IMGUI_FOLDER}imgui_widgets.cpp
   ${IMGUI_FOLDER}imstb_rectpack.h
   ${IMGUI_FOLDER}imstb_textedit.h
   ${IMGUI_FOLDER}imstb_truetype.h
   ${IMGUI_FOLDER}backends/imgui_impl_dx11.cpp
   ${IMGUI_FOLDER}backends/imgui_impl_dx11.h
   ${IMGUI_FOLDER}backends/imgui_impl_win32.cpp
   ${IMGUI_FOLDER}backends/imgui_impl_win32.h
   ${IMGUI_FOLDER}misc/debuggers/imgui.natvis
   ${IMGUI_FOLDER}misc/debuggers/imgui.natstepfilter
   ${IMGUI_FOLDER}misc/cpp/imgui_stdlib.cpp
   ${IMGUI_FOLDER}misc/cpp/imgui_stdlib.h
#  ------- SELECTION IMGUIZMO -------
   ${IMGUIZMO_FOLDER}GraphEditor.cpp
   ${IMGUIZMO_FOLDER}GraphEditor.h
   ${IMGUIZMO_FOLDER}ImCurveEdit.cpp
   ${IMGUIZMO_FOLDER}ImCurveEdit.h
   ${IMGUIZMO_FOLDER}ImCurveEdit.cpp
   ${IMGUIZMO_FOLDER}ImCurveEdit.h
   ${IMGUIZMO_FOLDER}ImGradient.cpp
   ${IMGUIZMO_FOLDER}ImGradient.h
   ${IMGUIZMO_FOLDER}ImGuizmo.cpp
   ${IMGUIZMO_FOLDER}ImGuizmo.h
   ${IMGUIZMO_FOLDER}ImSequencer.cpp
   ${IMGUIZMO_FOLDER}ImSequencer.h
   ${IMGUIZMO_FOLDER}ImZoomSlider.h
#  ------- SELECTION IMGUI NODE -------
   ${IMGUI_NODE_FOLDER}crude_json.cpp
   ${IMGUI_NODE_FOLDER}crude_json.h
   ${IMGUI_NODE_FOLDER}imgui_bezier_math.h
   ${IMGUI_NODE_FOLDER}imgui_canvas.cpp
   ${IMGUI_NODE_FOLDER}imgui_canvas.h
   ${IMGUI_NODE_FOLDER}imgui_extra_math.h
   ${IMGUI_NODE_FOLDER}imgui_node_editor.cpp
   ${IMGUI_NODE_FOLDER}imgui_node_editor.h
   ${IMGUI_NODE_FOLDER}imgui_node_editor.h
   ${IMGUI_NODE_FOLDER}imgui_node_editor_api.cpp
   ${IMGUI_NODE_FOLDER}imgui_node_editor_internal.h
   ${IMGUI_NODE_FOLDER}utilities/builders.cpp
   ${IMGUI_NODE_FOLDER}utilities/builders.h
   ${IMGUI_NODE_FOLDER}utilities/drawing.cpp
   ${IMGUI_NODE_FOLDER}utilities/drawing.h
   ${IMGUI_NODE_FOLDER}utilities/widgets.cpp
   ${IMGUI_NODE_FOLDER}utilities/widgets.h
)
add_library(GUI SHARED ${GUI_FILES} ${IMGUI_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${GUI_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR}"/../External" FILES ${IMGUI_FILES})
target_link_libraries(GUI PRIVATE
    Core
    Platform
    DirectXTex
)
target_include_directories(GUI PRIVATE
	"${GUI_FOLDER}"
    "${PLATFORM_FOLDER}"
	"${CORE_FOLDER}"
    "${EXTERNAL_FOLDER}imgui"
    "${EXTERNAL_FOLDER}ImGuizmo"
    "${EXTERNAL_FOLDER}imgui-node-editor"
    "${EXTERNAL_FOLDER}DirectXTex"
)
target_link_directories(GUI PRIVATE
    "${EXTERNAL_FOLDER}Lib"    
    ${CMAKE_BINARY_DIR}
)
target_compile_definitions(GUI PRIVATE ${COMMON_COMPILE_DEFINITIONS} HV_GUI_DLL)
target_compile_options(GUI PRIVATE /W3 /MP /ZI /JMC /fp:fast /FC)
target_link_options(GUI PRIVATE ${COMMON_LINK_OPTIONS})
set_property(TARGET GUI PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_target_properties(GUI PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
add_dependencies(GUI Core Platform)
# ==================== GUI ====================

# ==================== ENGINE ====================
set(ENGINE_FILES
	Engine/Timer.h
	Engine/Timer.cpp
	Engine/Threading/ThreadManager.h
	Engine/Threading/ThreadManager.cpp
	Engine/SequencerKeyframes/SequencerTransformKeyframe.h
	Engine/SequencerKeyframes/SequencerTransformKeyframe.cpp
	Engine/SequencerKeyframes/SequencerSpriteKeyframe.h
	Engine/SequencerKeyframes/SequencerSpriteKeyframe.cpp
	Engine/SequencerKeyframes/SequencerKeyframe.h
	Engine/SequencerKeyframes/SequencerKeyframe.cpp
	Engine/Scene/World.h
	Engine/Scene/World.cpp
	Engine/Scene/Scene.h
	Engine/Scene/Scene.cpp
	Engine/ModelImporter.h
	Engine/ModelImporter.cpp
	Engine/Input/InputTypes.h
	Engine/Input/InputMapper.h
	Engine/Input/InputMapper.cpp
	Engine/Input/Input.h
	Engine/Input/Input.cpp
	Engine/hvpch.h
	Engine/hvpch.cpp
	Engine/HexRune/Pin.h
	Engine/HexRune/Pin.cpp
	Engine/HexRune/NodeEditorContexts/ECSNodeEditorContexts.h
	Engine/HexRune/NodeEditorContexts/ECSNodeEditorContexts.cpp
	Engine/HexRune/NodeEditorContexts/CoreNodeEditorContexts.h
	Engine/HexRune/NodeEditorContexts/CoreNodeEditorContexts.cpp
	Engine/HexRune/NodeEditorContext.h
	Engine/HexRune/HexRune.h
	Engine/HexRune/HexRune.cpp
	Engine/HexRune/ECSNodes/ECSNodes.h
	Engine/HexRune/ECSNodes/ECSNodes.cpp
	Engine/HexRune/CoreNodes/CoreNodes.h
	Engine/HexRune/CoreNodes/CoreNodes.cpp
	Engine/HexPhys/HexPhys.h
	Engine/HexPhys/HexPhys.cpp
	Engine/Havtorn.h
	Engine/Graphics/TextureBank.h
	Engine/Graphics/TextureBank.cpp
	Engine/Graphics/RenderTextureFactory.h
	Engine/Graphics/RenderTextureFactory.cpp
	Engine/Graphics/RenderStateManager.h
	Engine/Graphics/RenderStateManager.cpp
	Engine/Graphics/RenderManager.h
	Engine/Graphics/RenderManager.cpp
	Engine/Graphics/RenderingPrimitives/RenderTexture.h
	Engine/Graphics/RenderingPrimitives/RenderTexture.cpp
	Engine/Graphics/RenderingPrimitives/GBuffer.h
	Engine/Graphics/RenderingPrimitives/GBuffer.cpp
	Engine/Graphics/RenderingPrimitives/DataBuffer.h
	Engine/Graphics/RenderingPrimitives/DataBuffer.cpp
	Engine/Graphics/Renderers/FullscreenRenderer.h
	Engine/Graphics/Renderers/FullscreenRenderer.cpp
	Engine/Graphics/RenderCommand.h
	Engine/Graphics/GraphicsUtilities.h
	Engine/Graphics/GraphicsUtilities.cpp
	Engine/Graphics/GraphicsStructs.h
	Engine/Graphics/GraphicsMaterial.h
	Engine/Graphics/GraphicsMaterial.cpp
	Engine/Graphics/GraphicsFramework.h
	Engine/Graphics/GraphicsFramework.cpp
	Engine/Graphics/GraphicsEnums.h
	Engine/Graphics/GeometryPrimitives.h
	Engine/Graphics/Debug/DebugDrawUtility.h
	Engine/Graphics/Debug/DebugDrawUtility.cpp
	Engine/FileSystem/FileWatcher.h
	Engine/FileSystem/FileWatcher.cpp
	Engine/Engine.h
	Engine/Engine.cpp
	Engine/ECS/Systems/SpriteAnimatorGraphSystem.h
	Engine/ECS/Systems/SpriteAnimatorGraphSystem.cpp
	Engine/ECS/Systems/SequencerSystem.h
	Engine/ECS/Systems/SequencerSystem.cpp
	Engine/ECS/Systems/ScriptSystem.h
	Engine/ECS/Systems/ScriptSystem.cpp
	Engine/ECS/Systems/RenderSystem.h
	Engine/ECS/Systems/RenderSystem.cpp
	Engine/ECS/Systems/LightSystem.h
	Engine/ECS/Systems/LightSystem.cpp
	Engine/ECS/Systems/DebugShapeSystem.h
	Engine/ECS/Systems/DebugShapeSystem.cpp
	Engine/ECS/Systems/CameraSystem.h
	Engine/ECS/Systems/CameraSystem.cpp
	Engine/ECS/Systems/AnimatorGraphSystem.h
	Engine/ECS/Systems/AnimatorGraphSystem.cpp
	Engine/ECS/System.h
	Engine/ECS/System.cpp
	Engine/ECS/GUIDManager.h
	Engine/ECS/GUIDManager.cpp
	Engine/ECS/Entity.h
	Engine/ECS/Entity.cpp
	Engine/ECS/ECSInclude.h
	Engine/ECS/Components/VolumetricLightComponent.h
	Engine/ECS/Components/TransformComponent.h
	Engine/ECS/Components/TransformComponent.cpp
	Engine/ECS/Components/Transform2DComponent.h
	Engine/ECS/Components/StaticMeshComponent.h
	Engine/ECS/Components/StaticMeshComponent.cpp
	Engine/ECS/Components/SpriteComponent.h
	Engine/ECS/Components/SpriteComponent.cpp
	Engine/ECS/Components/SpriteAnimatorGraphNode.h
	Engine/ECS/Components/SpriteAnimatorGraphNode.cpp
	Engine/ECS/Components/SpriteAnimatorGraphComponent.h
	Engine/ECS/Components/SpriteAnimatorGraphComponent.cpp
	Engine/ECS/Components/SpotLightComponent.h
	Engine/ECS/Components/SkeletalMeshComponent.h
	Engine/ECS/Components/SkeletalMeshComponent.cpp
	Engine/ECS/Components/SkeletalAnimationComponent.h
	Engine/ECS/Components/SkeletalAnimationComponent.cpp
	Engine/ECS/Components/SequencerComponent.h
	Engine/ECS/Components/ScriptComponent.h
	Engine/ECS/Components/ScriptComponent.cpp
	Engine/ECS/Components/PointLightComponent.h
	Engine/ECS/Components/Physics3DControllerComponent.h
	Engine/ECS/Components/Physics3DComponent.h
	Engine/ECS/Components/Physics2DComponent.h
	Engine/ECS/Components/MetaDataComponent.h
	Engine/ECS/Components/MaterialComponent.h
	Engine/ECS/Components/MaterialComponent.cpp
	Engine/ECS/Components/EnvironmentLightComponent.h
	Engine/ECS/Components/EnvironmentLightComponent.cpp
	Engine/ECS/Components/DirectionalLightComponent.h
	Engine/ECS/Components/DecalComponent.h
	Engine/ECS/Components/DecalComponent.cpp
	Engine/ECS/Components/DebugShapeComponent.h
	Engine/ECS/Components/CameraControllerComponent.h
	Engine/ECS/Components/CameraComponent.h
	Engine/ECS/ComponentEditorContexts/VolumetricLightComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/VolumetricLightComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/TransformComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/TransformComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/Transform2DComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/Transform2DComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/StaticMeshComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/StaticMeshComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/SpriteComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/SpriteComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/SpriteAnimatorGraphComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/SpriteAnimatorGraphComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/SpotLightComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/SpotLightComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/SkeletalMeshComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/SkeletalMeshComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/SkeletalAnimationComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/SkeletalAnimationComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/SequencerComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/SequencerComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/ScriptComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/ScriptComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/PointLightComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/PointLightComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/Physics3DControllerComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/Physics3DControllerComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/Physics3DComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/Physics3DComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/Physics2DComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/Physics2DComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/MaterialComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/MaterialComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/EnvironmentLightComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/EnvironmentLightComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/DirectionalLightComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/DirectionalLightComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/DecalComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/DecalComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/CameraControllerComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/CameraControllerComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContexts/CameraComponentEditorContext.h
	Engine/ECS/ComponentEditorContexts/CameraComponentEditorContext.cpp
	Engine/ECS/ComponentEditorContext.h
	Engine/ECS/ComponentAlgo.h
	Engine/ECS/Component.h
	Engine/ECS/Component.cpp
	Engine/Assets/SequencerAsset.h
	Engine/Assets/SequencerAsset.cpp
	Engine/Assets/RuntimeAssetDeclarations.h
	Engine/Assets/FileHeaderDeclarations.h
	Engine/Assets/AssetRegistry.h
	Engine/Assets/AssetRegistry.cpp
	Engine/Application/EngineProcess.h
	Engine/Application/EngineProcess.cpp
)

# ==================== ENGINE:SHADERS ====================
set(SHADER_INCLUDES
	Engine/Graphics/Shaders/Includes/VolumetricLightShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/SpriteShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/SpotLightShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/ShadowSampling.hlsli
	Engine/Graphics/Shaders/Includes/PointLightShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/PBRDirectLighting.hlsli
	Engine/Graphics/Shaders/Includes/PBRAmbientLighting.hlsli
	Engine/Graphics/Shaders/Includes/MathHelpers.hlsli
	Engine/Graphics/Shaders/Includes/LineShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/FullscreenShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/DetailNormalHelpers.hlsli
	Engine/Graphics/Shaders/Includes/DeferredShaderStructs.hlsli
	Engine/Graphics/Shaders/Includes/DeferredSamplingFunctions.hlsli
	Engine/Graphics/Shaders/Includes/DecalShaderStructs.hlsli
)
set(VERTEX_SHADERS
	Engine/Graphics/Shaders/SpriteInstanced_VS.hlsl
	Engine/Graphics/Shaders/SpriteInstancedEditor_VS.hlsl
	Engine/Graphics/Shaders/Skybox_VS.hlsl
	Engine/Graphics/Shaders/PointLight_VS.hlsl
	Engine/Graphics/Shaders/Line_VS.hlsl
	Engine/Graphics/Shaders/FullscreenVertexShader_VS.hlsl
	Engine/Graphics/Shaders/EditorPreview_VS.hlsl
	Engine/Graphics/Shaders/EditorPreviewSkeletal_VS.hlsl
	Engine/Graphics/Shaders/DeferredVertexPaint_VS.hlsl
	Engine/Graphics/Shaders/DeferredStaticMesh_VS.hlsl
	Engine/Graphics/Shaders/DeferredInstancedMesh_VS.hlsl
	Engine/Graphics/Shaders/DeferredInstancedMeshEditor_VS.hlsl
	Engine/Graphics/Shaders/DeferredInstancedAnimation_VS.hlsl
	Engine/Graphics/Shaders/DeferredInstancedAnimationEditor_VS.hlsl
	Engine/Graphics/Shaders/Decal_VS.hlsl
)
set(GEOMETRY_SHADERS
	Engine/Graphics/Shaders/SpriteWorldSpace_GS.hlsl
	Engine/Graphics/Shaders/SpriteWorldSpaceEditor_GS.hlsl
	Engine/Graphics/Shaders/SpriteScreenSpace_GS.hlsl
	Engine/Graphics/Shaders/Line_GS.hlsl
)
set(PIXEL_SHADERS
	Engine/Graphics/Shaders/SpriteWorldSpace_PS.hlsl
	Engine/Graphics/Shaders/SpriteWorldSpaceEditor_PS.hlsl
	Engine/Graphics/Shaders/SpriteWorldSpaceEditorWidget_PS.hlsl
	Engine/Graphics/Shaders/SpriteScreenSpace_PS.hlsl
	Engine/Graphics/Shaders/Skybox_PS.hlsl
	Engine/Graphics/Shaders/Line_PS.hlsl
	Engine/Graphics/Shaders/GBuffer_PS.hlsl
	Engine/Graphics/Shaders/GBufferEditor_PS.hlsl
	Engine/Graphics/Shaders/FullscreenVignette_PS.hlsl
	Engine/Graphics/Shaders/FullscreenTonemap_PS.hlsl
	Engine/Graphics/Shaders/FullscreenSSAO_PS.hlsl
	Engine/Graphics/Shaders/FullscreenSSAOBlur_PS.hlsl
	Engine/Graphics/Shaders/FullscreenMultiply_PS.hlsl
	Engine/Graphics/Shaders/FullscreenLuminance_PS.hlsl
	Engine/Graphics/Shaders/FullscreenGaussianBlurVertical_PS.hlsl
	Engine/Graphics/Shaders/FullscreenGaussianBlurHorizontal_PS.hlsl
	Engine/Graphics/Shaders/FullscreenGammaCorrection_PS.hlsl
	Engine/Graphics/Shaders/FullscreenFXAA_PS.hlsl
	Engine/Graphics/Shaders/FullscreenEditorData_PS.hlsl
	Engine/Graphics/Shaders/FullscreenDifference_PS.hlsl
	Engine/Graphics/Shaders/FullscreenDepthDownSample_PS.hlsl
	Engine/Graphics/Shaders/FullscreenDepthAwareUpsample_PS.hlsl
	Engine/Graphics/Shaders/FullscreenCopy_PS.hlsl
	Engine/Graphics/Shaders/FullscreenCopyGBuffer_PS.hlsl
	Engine/Graphics/Shaders/FullscreenCopyDepth_PS.hlsl
	Engine/Graphics/Shaders/FullscreenBloom_PS.hlsl
	Engine/Graphics/Shaders/FullscreenBilateralBlurVertical_PS.hlsl
	Engine/Graphics/Shaders/FullscreenBilateralBlurHorizontal_PS.hlsl
	Engine/Graphics/Shaders/EditorPreview_PS.hlsl
	Engine/Graphics/Shaders/DeferredVertexPaint_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassRoughness_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassNormal_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassMetalness_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassGBuffer_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassFullscreenGammaCorrection_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassEmissive_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassAO_PS.hlsl
	Engine/Graphics/Shaders/DeferredRenderPassAlbedo_PS.hlsl
	Engine/Graphics/Shaders/DeferredLightSpot_PS.hlsl
	Engine/Graphics/Shaders/DeferredLightSpotVolumetric_PS.hlsl
	Engine/Graphics/Shaders/DeferredLightPoint_PS.hlsl
	Engine/Graphics/Shaders/DeferredLightPointVolumetric_PS.hlsl
	Engine/Graphics/Shaders/DeferredLightDirectionalVolumetric_PS.hlsl
	Engine/Graphics/Shaders/DeferredLightDirectionalAndEnvironment_PS.hlsl
	Engine/Graphics/Shaders/Decal_Normal_PS.hlsl
	Engine/Graphics/Shaders/Decal_Material_PS.hlsl
	Engine/Graphics/Shaders/Decal_Albedo_PS.hlsl
)
set_source_files_properties(${VERTEX_SHADERS} PROPERTIES VS_SHADER_TYPE Vertex)
set_source_files_properties(${GEOMETRY_SHADERS} PROPERTIES VS_SHADER_TYPE Geometry)
set_source_files_properties(${PIXEL_SHADERS} PROPERTIES VS_SHADER_TYPE Pixel)
set(HLSL_SHADER_FILES
    ${VERTEX_SHADERS}
    ${GEOMETRY_SHADERS}
    ${PIXEL_SHADERS}
)
set_source_files_properties(${HLSL_SHADER_FILES} PROPERTIES VS_SHADER_MODEL 5.0)
foreach(FILE ${HLSL_SHADER_FILES})
  get_filename_component(FILE_NAME ${FILE} NAME_WE)
  set_property(SOURCE ${FILE} PROPERTY VS_SHADER_OBJECT_FILE_NAME ${WORKING_FOLDER}Shaders/${FILE_NAME}.cso)
endforeach(FILE)
# ==================== ENGINE:SHADERS ====================

add_library(Engine SHARED ${ENGINE_FILES} ${SHADER_INCLUDES} ${HLSL_SHADER_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${ENGINE_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${SHADER_INCLUDES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${HLSL_SHADER_FILES})
target_link_libraries(Engine PRIVATE
    assimp-vc143-mtd
    DirectXTex
    box2dd
    PhysX/PhysX_64
    PhysX/PhysXCommon_64
    PhysX/PhysXExtensions_static_64
    PhysX/PhysXFoundation_64
    PhysX/PhysXPvdSDK_static_64
    PhysX/PhysXCharacterKinematic_static_64
    Core
    Platform
    GUI
)
target_include_directories(Engine PRIVATE
    "${ENGINE_FOLDER}"
    "${EXTERNAL_FOLDER}"
    "${EXTERNAL_FOLDER}assimp/include"
    "${EXTERNAL_FOLDER}FastNoise2/include"
    "${EXTERNAL_FOLDER}rapidjson/include"
    "${EXTERNAL_FOLDER}DirectXTex"
    "${EXTERNAL_FOLDER}box2d/include/box2d"
    "${EXTERNAL_FOLDER}box2dcpp/include/box2cpp"
    "${EXTERNAL_FOLDER}PhysX/physx/include"
    "Core"
    "Platform"
    "GUI"
)
target_link_directories(Engine PRIVATE
    "${EXTERNAL_FOLDER}Lib"
    ${CMAKE_BINARY_DIR}
)
target_compile_definitions(Engine PRIVATE ${COMMON_COMPILE_DEFINITIONS} HV_ENGINE_DLL)
target_compile_options(Engine PRIVATE ${COMMON_COMPILE_OPTIONS})
target_compile_options(Engine PRIVATE "/FI${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/Engine.dir/$<CONFIG>/cmake_pch.hxx")
target_precompile_headers(Engine PRIVATE ${ENGINE_FOLDER}hvpch.h)
target_link_options(Engine PRIVATE ${COMMON_LINK_OPTIONS} /NODEFAULTLIB:LIBCMTD.lib)
#target_link_options(Engine PRIVATE ${COMMON_LINK_OPTIONS} /NODEFAULTLIB:LIBCMTD.lib /IMPLIB:${CMAKE_CURRENT_BINARY_DIR}/Engine.dir/Engine/Engine_$<CONFIG>.lib)
set_property(TARGET Engine PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_target_properties(Engine PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
add_dependencies(Engine Core Platform GUI)
# ==================== ENGINE ====================


# ==================== GAME ====================
set(GAME_FILES
	Game/hvpch.h
	Game/hvpch.cpp
	Game/Ghosty/GhostySystem.h
	Game/Ghosty/GhostySystem.cpp
	Game/Ghosty/GhostyComponentEditorContext.h
	Game/Ghosty/GhostyComponentEditorContext.cpp
	Game/Ghosty/GhostyComponent.h
	Game/GameScript.h
	Game/GameScript.cpp
	Game/GameScene.h
	Game/GameScene.cpp
	Game/GameProcess.h
	Game/GameProcess.cpp
	Game/GameManager.h
	Game/GameManager.cpp
)
add_library(Game SHARED ${GAME_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${GAME_FILES})
target_include_directories(Game PRIVATE
    "${GAME_FOLDER}"
    "${EXTERNAL_FOLDER}"
    "${EXTERNAL_FOLDER}FastNoise2/include"
    "${EXTERNAL_FOLDER}rapidjson/include"
    "${EXTERNAL_FOLDER}DirectXTex"
    "${EXTERNAL_FOLDER}box2d/include/box2d"
    "${EXTERNAL_FOLDER}box2dcpp/include/box2cpp"
    "${EXTERNAL_FOLDER}PhysX/physx/include"
    "Core"
    "Platform"
    "GUI"
    "Engine"
)
target_link_libraries(Game PRIVATE
    Core
    Platform
    GUI
    Engine
)
target_link_directories(Game PRIVATE
    ${CMAKE_BINARY_DIR}
)
target_compile_definitions(Game PRIVATE ${COMMON_COMPILE_DEFINITIONS} HV_GAME_DLL)
target_compile_options(Game PRIVATE ${COMMON_COMPILE_OPTIONS})
target_compile_options(Game PRIVATE "/FI${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/Game.dir/$<CONFIG>/cmake_pch.hxx")
target_precompile_headers(Game PRIVATE ${GAME_FOLDER}hvpch.h)
target_link_options(Game PRIVATE ${COMMON_LINK_OPTIONS})
set_property(TARGET Game PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_target_properties(Game PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
add_dependencies(Game Core Platform GUI Engine)
# ==================== GAME ====================

# ==================== EDITOR ====================
set(EDITOR_FILES
	Editor/Windows/ViewportWindow.h
	Editor/Windows/ViewportWindow.cpp
	Editor/Windows/SpriteAnimatorGraphNodeWindow.h
	Editor/Windows/SpriteAnimatorGraphNodeWindow.cpp
	Editor/Windows/SequencerWindow.h
	Editor/Windows/SequencerWindow.cpp
	Editor/Windows/OutputLogWindow.h
	Editor/Windows/OutputLogWindow.cpp
	Editor/Windows/InspectorWindow.h
	Editor/Windows/InspectorWindow.cpp
	Editor/Windows/HierarchyWindow.h
	Editor/Windows/HierarchyWindow.cpp
	Editor/Windows/DockSpaceWindow.h
	Editor/Windows/DockSpaceWindow.cpp
	Editor/Windows/AssetBrowserWindow.h
	Editor/Windows/AssetBrowserWindow.cpp
	Editor/Toggleables/WindowMenu.h
	Editor/Toggleables/WindowMenu.cpp
	Editor/Toggleables/ViewMenu.h
	Editor/Toggleables/ViewMenu.cpp
	Editor/Toggleables/HelpMenu.h
	Editor/Toggleables/HelpMenu.cpp
	Editor/Toggleables/FileMenu.h
	Editor/Toggleables/FileMenu.cpp
	Editor/Toggleables/EditMenu.h
	Editor/Toggleables/EditMenu.cpp
	Editor/Systems/PickingSystem.h
	Editor/Systems/PickingSystem.cpp
	Editor/Systems/EditorRenderSystem.h
	Editor/Systems/EditorRenderSystem.cpp
	Editor/hvpch.h
	Editor/hvpch.cpp
	Editor/EditorWindows.h
	Editor/EditorWindow.h
	Editor/EditorWindow.cpp
	Editor/EditorToggleables.h
	Editor/EditorToggleable.h
	Editor/EditorToggleable.cpp
	Editor/EditorResourceManager.h
	Editor/EditorResourceManager.cpp
	Editor/EditorProcess.h
	Editor/EditorProcess.cpp
	Editor/EditorManager.h
	Editor/EditorManager.cpp
	Editor/AuthoringTools/ScriptTool.h
	Editor/AuthoringTools/ScriptTool.cpp
	Editor/AuthoringTools/MaterialTool.h
	Editor/AuthoringTools/MaterialTool.cpp
)
add_library(Editor SHARED ${EDITOR_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${EDITOR_FILES})
target_include_directories(Editor PRIVATE
    "${EDITOR_FOLDER}"
    "${EXTERNAL_FOLDER}rapidjson/include"
    "${EXTERNAL_FOLDER}DirectXTex"
    "${EXTERNAL_FOLDER}box2d/include/box2d"
    "${EXTERNAL_FOLDER}box2dcpp/include/box2cpp"
    "${EXTERNAL_FOLDER}PhysX/physx/include"
    "Core"
    "Platform"
    "GUI"
    "Engine"
)
target_link_libraries(Editor PRIVATE
    Core
    Platform
    GUI
    Engine
    Game
)
target_link_directories(Editor PRIVATE
    ${CMAKE_BINARY_DIR}
)
target_compile_definitions(Editor PRIVATE ${COMMON_COMPILE_DEFINITIONS} HV_EDITOR_DLL)
target_compile_options(Editor PRIVATE ${COMMON_COMPILE_OPTIONS})
target_precompile_headers(Editor PRIVATE ${EDITOR_FOLDER}hvpch.h)
target_link_options(Editor PRIVATE ${COMMON_LINK_OPTIONS})
set_property(TARGET Editor PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_target_properties(Editor PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
add_dependencies(Editor Core Platform GUI Engine Game)
# ==================== EDITOR ====================

# ==================== LAUNCHER ====================
set(LAUNCHER_FILES
	Launcher/Main.cpp
	Launcher/Application/Process.h
	Launcher/Application/Application.h
	Launcher/Application/Application.cpp
)
add_executable(Launcher WIN32 ${LAUNCHER_FILES})
source_group(TREE ${CMAKE_CURRENT_SOURCE_DIR} FILES ${LAUNCHER_FILES})
target_include_directories(Launcher PRIVATE
	"${LAUNCHER_FOLDER}"
    "${EXTERNAL_FOLDER}box2d/include/box2d"
    "${EXTERNAL_FOLDER}rapidjson/include"
	"${EXTERNAL_FOLDER}box2dcpp/include/box2cpp"
	"${EXTERNAL_FOLDER}PhysX/physx/include"
    "Core"
    "Platform"
	"GUI"
	"Engine"
	"Game"
	"Editor"
)
target_link_libraries(Launcher PRIVATE
    Core    
    Platform
    GUI
    Engine
    Game
    Editor
)
target_link_directories(Launcher PRIVATE
    ${CMAKE_BINARY_DIR}
)
target_compile_definitions(Launcher PRIVATE ${COMMON_COMPILE_DEFINITIONS})
target_compile_options(Launcher PRIVATE ${COMMON_COMPILE_OPTIONS})
target_link_options(Launcher PRIVATE ${COMMON_LINK_OPTIONS})
set_property(TARGET Launcher PROPERTY VS_DEBUGGER_WORKING_DIRECTORY ${WORKING_FOLDER})
set_property(DIRECTORY PROPERTY VS_STARTUP_PROJECT Launcher)
set_target_properties(Launcher PROPERTIES RUNTIME_OUTPUT_DIRECTORY_DEBUG ${WORKING_FOLDER} RUNTIME_OUTPUT_DIRECTORY_RELEASE ${WORKING_FOLDER})
add_dependencies(Launcher Core Platform GUI Engine Game Editor)
# ==================== LAUNCHER ====================
