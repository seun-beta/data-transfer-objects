# Data Transfer Object Implementation

## Table of Contents

- [About](#about)
- [UML Diagram](#uml)


## About <a name = "about"></a>

A Data Transfer Object (DTO) is an object that carries data between processes. The motivation for its use is that communication between processes is usually done resorting to remote interfaces (e.g., web services), where each call is an expensive operation. Because the majority of the cost of each call is related to the round-trip time between the client and the server, one way of reducing the number of calls is to use an object (the DTO) that aggregates the data that would have been transferred by the several calls, but that is served by one call only.


The aim of this project is to do the following:
- Implement a DTO, 
- Test my understanding of DTOs
- Write unit tests for the DTO
- Utilize python type hints

## Unified Modeling Language Diagram of the DTO <a name="uml"></a>

![UML Diagram of the DTO](https://github.com/seun-beta/data-transfer-objects/blob/main/assets/uml.png?raw=true)
