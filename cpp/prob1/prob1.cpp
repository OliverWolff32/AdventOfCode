#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string line;
    int max = 0;
    ifstream myfile ("prob1.txt");
    int sum = 0;
    while(getline(myfile, line)) {
        if(line != "") {
            sum += stoi(line);
        } else {
            if(sum > max) {
                max = sum;
            }
            sum = 0;
        }
    }
    cout << max;
    return 0;
}