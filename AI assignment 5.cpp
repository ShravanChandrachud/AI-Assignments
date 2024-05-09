#include <iostream>
#include <string>
#include <algorithm> // Include the algorithm header for the transform
using namespace std;
// Function to generate a generic response
string generateResponse(const string &userQuery)
{
    // Simple mapping of user queries to bot responses
    if (userQuery.find("shampoo") != string::npos)
    {
        return "Our range of shampoos includes options for all hair types,from dry to oily.";
    }
    else if (userQuery.find("conditioner") != string::npos)
    {
        return "Our conditioners are designed to nourish and hydrate your hair,leaving it soft and silky.";
    }
    else if (userQuery.find("hair mask") != string::npos)
    {
        return "Our hair masks are perfect for deep conditioning and repairing damaged hair.";
    }
    else if (userQuery.find("hair serum") != string::npos)
    {
        return "Our hair serums add shine and manageability to your hair,while also protecting it from heat damage.";
    }
    else
    {
        return "I'm sorry, I'm not sure how to help with that. Can you please provide more details? ";
    }
}
int main()
{
    cout << "Welcome to Haircare Products Support. How can I assist you today? " << endl;
    cout << "You can ask about our products, recommendations, or any other queries you have." << endl;
    cout << "Type 'exit' to end the conversation." << endl;
    string userQuery;
    while (true)
    {
        cout << "You: ";
        getline(cin, userQuery);
        // Convert user input to lowercase for case-insensitive comparison
        transform(userQuery.begin(), userQuery.end(), userQuery.begin(), ::tolower);
        // Exit condition
        if (userQuery == "exit")
        {
            cout << "Goodbye! Have a great hair day!" << endl;
            break;
        }
        // Generate bot response based on user query
        string response = generateResponse(userQuery);
        cout << "Bot: " << response << endl;
    }
    return 0;
}