// Copyright 2023 Team Havtorn. All Rights Reserved.

#pragma once

#include "Graphics/LineShape.h"

namespace Havtorn
{
	struct SDebugShape
	{
		SMatrix Matrix;
		SLineShape LineShape;
		F32 LifeTime = 0.0f;

		const bool operator<(const SDebugShape& rhs) const { return LifeTime < rhs.LifeTime; }
		const bool operator>(const SDebugShape& rhs) const { return LifeTime > rhs.LifeTime; }
	};
}
