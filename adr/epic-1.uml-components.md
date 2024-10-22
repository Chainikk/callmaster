@startuml
package "Model Layer" {
  [Data Models]
  [Business Logic]
  [Database Access]
  [Validation Rules]
}

package "Controller Layer" {
  [Routing] --> [Action Methods]
  [Action Methods] --> [Data Transformation]
  [Action Methods] --> [Session Management]
  [Action Methods] --> [Request Handlers]
}

package "View Layer" {
  [Templates] --> [Template Engine]
  [Template Engine] --> [User Interface]
}

database Database
[Database Access] --> Database : Reads/Writes Data

@enduml
