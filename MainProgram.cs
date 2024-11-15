using System;
using System.Globalization;
using FinalAssignment;

namespace MainProgram
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length != 1)
            {
                Console.WriteLine("Please provide a single file path argument.");
                return;
            }

            string filePath = args[0];
            if (!File.Exists(filePath))
            {
                Console.WriteLine("File not found.");
                return;
            }

            try
            {
                double result = Solver.ProcessFile(filePath);
                Console.WriteLine("The sum of measurements is {0:N2}.", result);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error processing file: {ex.Message}");
            }
        }
    }
}
