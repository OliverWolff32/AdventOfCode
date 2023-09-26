#include <iostream> 
#include <fstream> 

using namespace std;

int main() {
    string line; 
    int totalScore = 0; 
    int score; 
    ifstream myfile ("OliverProb2Input.txt");

    while(getline(myfile, line)) {
        if(line[0] == 'A') { // rock
            if(line[2] == 'X') { 
                score += 3; // scissors
                score += 0; // lose
            }
            if(line[2] == 'Y') { 
                score += 1; // rock
                score += 3; // draw
            }
            if(line[2] == 'Z') { 
                score += 2; // paper
                score += 6; // win
            }
        }
        if(line[0] == 'B') { // paper
            if(line[2] == 'X') { 
                score += 1; // rock
                score += 0; // lose
            }
            if(line[2] == 'Y') { 
                score += 2; // paper
                score += 3; // draw
            }
            if(line[2] == 'Z') { 
                score += 3; // scissors
                score += 6; // win
            }
        }
        if(line[0] == 'C') { // scissors
            if(line[2] == 'X') { 
                score += 2; // paper
                score += 0; // lose
            }
            if(line[2] == 'Y') { 
                score += 3; // scissors
                score += 3; // draw
            }
            if(line[2] == 'Z') { 
                score += 1; // rock
                score += 6; // win
            }
        }
        totalScore += score;
        score = 0;
    }
    cout << totalScore << endl;
    return 0;
}