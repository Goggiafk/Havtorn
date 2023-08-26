// Copyright 2022 Team Havtorn. All Rights Reserved.

#pragma once

#include "Core/Color.h"

namespace Havtorn
{
	struct SLineShape
	{
		SColor Color;
		F32 Thickness = 1.0f;
		U16 IndexCount = 0;
		U8 VertexBufferIndex = 0;
		U8 IndexBufferIndex = 0;
		bool IgnoreDepth = true;
	};
}
