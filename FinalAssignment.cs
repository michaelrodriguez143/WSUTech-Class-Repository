using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using Shapes3D;

namespace FinalAssignment
{
    public static class Solver
    {
        public static double ProcessFile(string filePath)
        {
            var shapes = new List<Shape3D>();
            double totalMeasurement = 0;

            foreach (var line in File.ReadLines(filePath))
            {
                var parts = line.Split(',');

                switch (parts[0].Trim().ToLower())
                {
                    case "cube":
                        shapes.Add(new Cube(double.Parse(parts[1], CultureInfo.InvariantCulture)));
                        break;
                    case "cuboid":
                        shapes.Add(new Cuboid(double.Parse(parts[1], CultureInfo.InvariantCulture),
                                              double.Parse(parts[2], CultureInfo.InvariantCulture),
                                              double.Parse(parts[3], CultureInfo.InvariantCulture)));
                        break;
                    case "cylinder":
                        shapes.Add(new Cylinder(double.Parse(parts[1], CultureInfo.InvariantCulture),
                                                double.Parse(parts[2], CultureInfo.InvariantCulture)));
                        break;
                    case "sphere":
                        shapes.Add(new Sphere(double.Parse(parts[1], CultureInfo.InvariantCulture)));
                        break;
                    case "prism":
                        shapes.Add(new Prism(double.Parse(parts[1], CultureInfo.InvariantCulture),
                                             int.Parse(parts[2], CultureInfo.InvariantCulture),
                                             double.Parse(parts[3], CultureInfo.InvariantCulture)));
                        break;
                    case "area":
                    case "volume":
                        double scale = double.Parse(parts[1], CultureInfo.InvariantCulture);
                        double sum = 0;
                        foreach (var shape in shapes)
                        {
                            sum += parts[0].Trim().ToLower() == "area" ? shape.SurfaceArea : shape.Volume;
                        }
                        totalMeasurement += sum * scale;
                        shapes.Clear(); // Clear shapes after calculating
                        break;
                }
            }

            return totalMeasurement;
        }
    }
}
