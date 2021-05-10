<p align='center'>
<img src='../../../_images/logo.png' width='512px'/>
</p>

# RectF

<p align='left'>
<img src='https://img.shields.io/badge/type-class-green' />
<img src='https://img.shields.io/badge/since-1.0.0-green' />
</p>

Stores a set of four floating-point numbers that represent the location and size of a rectangle.

## Methods

### `__init__()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `None`

### `__init__(pt1,pt2)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt1: [PointF](./PointF.md)
  - pt2: [PointF](./PointF.md)
- returnType: `None`

### `__init__(pt,width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
  - width: `float`
  - height: `float`
- returnType: `None`

### `__init__(left,top,right,bottom)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `float`
  - top: `float`
  - right: `float`
  - bottom: `float`
- returnType: `None`

### `__str__()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `str`

### `Reset()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `None`

### `Set(rect)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - rect: `RectF`
- returnType: `None`

### `Set(pt1,pt2)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt1: [PointF](./PointF.md)
  - pt2: [PointF](./PointF.md)
- returnType: `None`

### `Set(pt,width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
  - width: `float`
  - height: `float`
- returnType: `None`

### `Set(left,top,right,bottom)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `float`
  - top: `float`
  - right: `float`
  - bottom: `float`
- returnType: `None`

### `SetWithSize(left,top,width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `float`
  - top: `float`
  - width: `float`
  - height: `float`
- returnType: `None`

### `SetLeft(left)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `float`
- returnType: `None`

### `GetLeft()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `float`

### `SetTop(top)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - top: `float`
- returnType: `None`

### `GetTop()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `float`

### `SetRight(right)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - right: `float`
- returnType: `None`

### `GetRight()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `float`

### `SetBottom(bottom)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - bottom: `float`
- returnType: `None`

### `GetBottom()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `float`

### `SetLeftTop(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
- returnType: `None`

### `GetLeftTop()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [PointF](./PointF.md)

### `SetLeftBottom(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
- returnType: `None`

### `GetLeftBottom()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [PointF](./PointF.md)

### `SetRightTop(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
- returnType: `None`

### `GetRightTop()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [PointF](./PointF.md)

### `SetRightBottom(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
- returnType: `None`

### `GetRightBottom()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [PointF](./PointF.md)

### `SetCenter(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
- returnType: `None`

### `GetCenter()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [PointF](./PointF.md)

### `SetWidth(width)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - width: `float`
- returnType: `None`

### `GetWidth()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `float`

### `SetHeight(height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - height: `float`
- returnType: `None`

### `GetHeight()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `float`

### `SetSize(width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - width: `float`
  - height: `float`
- returnType: `None`

### `Offset(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `float`
  - dy: `float`
- returnType: `None`

### `Resize(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `float`
  - dy: `float`
- returnType: `None`

### `Inflate(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `float`
  - dy: `float`
- returnType: `None`

### `Inset(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `float`
  - dy: `float`
- returnType: `None`

### `IsEmpty()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `boolean`

### `Scale(factor)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - factor：`float`
- returnType: `RectF`

### `IsIntersecting(other)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - other: `RectF`
- returnType: `boolean`

### `Contains(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [PointF](./PointF.md)
- returnType: `boolean`

### `Contains(x,y)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - x: `float`
  - y: `float`
- returnType: `boolean`

### `Contains(in)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - in: `RectF`
- returnType: `boolean`

### `Union(other)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - other: `RectF`
- returnType: `RectF`

### `Intersect(other)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - other: `RectF`
- returnType: `RectF`
