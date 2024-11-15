using System;
using Shapes;

namespace Shapes3D
{
    public abstract class Shape3D
    {
        public abstract double SurfaceArea { get; }
        public abstract double Volume { get; }
    }

    public class Cuboid : Shape3D
    {
        private double width, height, depth;
        public Cuboid(double width, double height, double depth)
        {
            this.width = width;
            this.height = height;
            this.depth = depth;
        }

        public override double SurfaceArea => 2 * (width * height + height * depth + width * depth);
        public override double Volume => width * height * depth;
    }

    public class Cube : Cuboid
    {
        public Cube(double sideLength) : base(sideLength, sideLength, sideLength) { }
    }

    public class Cylinder : Shape3D
    {
        private double radius, height;
        public Cylinder(double radius, double height)
        {
            this.radius = radius;
            this.height = height;
        }

        public override double SurfaceArea => 2 * Math.PI * radius * (radius + height);
        public override double Volume => Math.PI * Math.Pow(radius, 2) * height;
    }

    public class Sphere : Shape3D
    {
        private double radius;
        public Sphere(double radius)
        {
            this.radius = radius;
        }

        public override double SurfaceArea => 4 * Math.PI * Math.Pow(radius, 2);
        public override double Volume => (4.0 / 3) * Math.PI * Math.Pow(radius, 3);
    }

    public class Prism : Shape3D
    {
        private double surfaceArea, volume;
        public Prism(double sideLength, int faces, double height)
        {
            Polygon basePolygon = new Polygon(sideLength, faces);
            surfaceArea = 2 * basePolygon.Area() + basePolygon.Perimeter() * height;
            volume = basePolygon.Area() * height;
        }

        public override double SurfaceArea => surfaceArea;
        public override double Volume => volume;
    }
}
