\# Testing Strategy



\## Overview



This project uses a multi-layered testing strategy consisting of unit tests and integration tests.



\- Unit tests verify the correctness of individual calculator functions.

\- Integration tests verify the interaction between the application layer and the calculation logic.



---



\## What Was Tested



\- Addition

\- Subtraction

\- Multiplication

\- Division

\- Division by zero handling

\- Edge cases (negative, decimal, very large numbers)

\- Clear function behavior

\- Full user flow for addition



---



\## What Was Not Tested



\- UI/visual interface (not required for this assignment)

\- Performance testing

\- Security testing



The focus of this project is functional correctness.



---



\# Lecture Concepts



\## Testing Pyramid



The test suite follows the testing pyramid principle:

\- Majority are unit tests (fast and isolated)

\- Fewer integration tests verify component interaction



---



\## Black-box vs White-box Testing



Unit tests are closer to white-box testing because they directly test internal functions.



Integration tests simulate application behavior and resemble black-box testing.



---



\## Functional vs Non-Functional Testing



This project focuses on functional testing (correct results).



Non-functional aspects like performance and usability were intentionally not tested.



---



\## Regression Testing



Running:



python -m pytest



after any change ensures regressions are caught and previous functionality remains correct.



---



\# Test Results Summary



| Test Name | Type | Status |

|-----------|------|--------|

| test\_add | Unit | Pass |

| test\_subtract | Unit | Pass |

| test\_multiply | Unit | Pass |

| test\_divide | Unit | Pass |

| test\_divide\_by\_zero | Unit | Pass |

| test\_negative\_numbers | Unit | Pass |

| test\_decimal\_numbers | Unit | Pass |

| test\_large\_numbers | Unit | Pass |

| test\_full\_user\_flow\_addition | Integration | Pass |

| test\_clear\_resets\_to\_zero | Integration | Pass |

