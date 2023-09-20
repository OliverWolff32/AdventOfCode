#include <iostream> 
#include <fstream> 

using namespace std;


int main() {
    ifstream myfile ("OliverProb4Input.txt");
    string line; 
    int nums[4]; 
    int numsLength = 4; 

    while(getline(myfile, line)) {
        for (int i = 0; i < numsLength; i++) {
            for(char ch : line) {
                if(ch == '-') break; 
                nums[i] *= 10; 
                nums[i] += ch - '0'; // ch to int w ascii

            }
        }
    }
    cout << nums << endl;
    return 0;
}