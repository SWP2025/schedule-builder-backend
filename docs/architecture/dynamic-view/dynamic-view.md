## Dynamic view
```mermaid
sequenceDiagram
    title "/collisions/check" request

    actor User
    participant Frontend
    participant Router
    participant Authorizer
    participant Parser
    participant Outlook API
    participant Validator

    User->>Frontend:Pressing button "Check Scheduling" in the plugin
    Frontend->>Router:Request to API from Google Spreadsheets

    Router->>Authorizer:User Authorization via token
    Authorizer->>Parser:Parsing data from Google Spreadsheets
    Parser->>Validator:Passing data to check for scheduling collisions
    Authorizer->>Outlook API:Getting information about events to compare from Outlook API
    Parser->>Validator:Passing data to check collisions
    Validator->>Router:Returning collisions in expected format
    Router->>Frontend:Returning response to the extension
    Frontend->>User:Showing result to the user
```

We tested the scenario and conducted that it takes up to `10 seconds` to execute in our product environment.
