<p align='center'>
<img src='../../../_images/logo.png' width='512px'/>
</p>

# Rect

<p align='left'>
<img src='https://img.shields.io/badge/type-class-green' />
<img src='https://img.shields.io/badge/since-1.0.0-green' />
</p>

Stores a set of four integers that represent the location and size of a rectangle.

## Methods

### `__init__()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `None`

### `__init__(pt1,pt2)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt1: [Point](./Point.md)
  - pt2: [Point](./Point.md)
- returnType: `None`

### `__init__(pt,width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
  - width: `int`
  - height: `int`
- returnType: `None`

### `__init__(left,top,right,bottom)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `int`
  - top: `int`
  - right: `int`
  - bottom: `int`
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
  - rect: `Rect`
- returnType: `None`

### `Set(pt1,pt2)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt1: [Point](./Point.md)
  - pt2: [Point](./Point.md)
- returnType: `None`

### `Set(pt,width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
  - width: `int`
  - height: `int`
- returnType: `None`

### `Set(left,top,right,bottom)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `int`
  - top: `int`
  - right: `int`
  - bottom: `int`
- returnType: `None`

### `SetWithSize(left,top,width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `int`
  - top: `int`
  - width: `int`
  - height: `int`
- returnType: `None`

### `SetLeft(left)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - left: `int`
- returnType: `None`

### `GetLeft()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `int`

### `SetTop(top)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - top: `int`
- returnType: `None`

### `GetTop()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `int`

### `SetRight(right)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - right: `int`
- returnType: `None`

### `GetRight()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `int`

### `SetBottom(bottom)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - bottom: `int`
- returnType: `None`

### `GetBottom()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `int`

### `SetLeftTop(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
- returnType: `None`

### `GetLeftTop()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [Point](./Point.md)

### `SetLeftBottom(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
- returnType: `None`

### `GetLeftBottom()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [Point](./Point.md)

### `SetRightTop(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
- returnType: `None`

### `GetRightTop()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [Point](./Point.md)

### `SetRightBottom(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
- returnType: `None`

### `GetRightBottom()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [Point](./Point.md)

### `SetCenter(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
- returnType: `None`

### `GetCenter()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: [Point](./Point.md)

### `SetWidth(width)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - width: `int`
- returnType: `None`

### `GetWidth()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `int`

### `SetHeight(height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - height: `int`
- returnType: `None`

### `GetHeight()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `int`

### `SetSize(width,height)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - width: `int`
  - height: `int`
- returnType: `None`

### `Offset(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `int`
  - dy: `int`
- returnType: `None`

### `Resize(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `int`
  - dy: `int`
- returnType: `None`

### `Inflate(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `int`
  - dy: `int`
- returnType: `None`

### `Inset(dx,dy)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - dx: `int`
  - dy: `int`
- returnType: `None`

### `IsEmpty()`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters: `None`
- returnType: `boolean`

### `Scale(factor)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - factor：`float`
- returnType: `Rect`

### `IsIntersecting(other)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - other: `Rect`
- returnType: `boolean`

### `Contains(pt)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - pt: [Point](./Point.md)
- returnType: `boolean`

### `Contains(x,y)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - x: `int`
  - y: `int`
- returnType: `boolean`

### `Contains(in)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - in: `Rect`
- returnType: `boolean`

### `Union(other)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - other: `Rect`
- returnType: `Rect`

### `Intersect(other)`

![1.0.0](https://img.shields.io/badge/since-1.0.0-green)

- parameters:
  - other: `Rect`
- returnType: `Rect`
