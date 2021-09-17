#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int n; cin >> n;
    string s;
    vector<string> vec;
    for(int i = 0; i < n; i++){
        cin >> s;
        vec.push_back(s);
    }
    for(int i = 0; i < n; i++){
        cout << s[i];
    }
}