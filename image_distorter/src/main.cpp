#include <iostream>
#include <string>
/*
    A basic implementation of reading in a png and distorting the image
*/
int PGRM_NAME_IDX = 0;
int INPUT_FILE_ARG_IDX = 1;
int OUTPUT_FILE_ARG_IDX = 2;
int MINIMUM_ARG_LENGTH = 2;

int main(int argc, char** argv) {

    // argc includes the program name
    if (argc < MINIMUM_ARG_LENGTH) {
        std::cerr << "Usage: " << argv[PGRM_NAME_IDX] << " <input_file> [output_file]\n";
        return 1;
    }

    std::string inputFile  = argv[INPUT_FILE_ARG_IDX];
    std::string outputFile;

    if (argc >= 3) {
        outputFile = argv[OUTPUT_FILE_ARG_IDX];
    } else {
        outputFile = "output.png";  // default name
    }

    std::cout << "Input file:  " << inputFile  << "\n";
    std::cout << "Output file: " << outputFile << "\n";

    // TODO: load image, decode it, process it, write output, etc.
    // e.g. loadPNG(inputFile, ...)

    return 0;
}
