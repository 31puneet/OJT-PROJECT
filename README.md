1. Mini CMS – Page Version History & Comparison UI
By: Puneet Seervi & Aditya Aryan Poddar

2. Project Overview
This project aims to make content editing inside a CMS easier and safer. When multiple users edit the same page, it becomes difficult to know what changed, who changed it, or how to recover an older version.
Our solution provides an interface where users can browse past versions, compare them visually, and restore any version whenever needed.

3. Problem Statement
In most CMS systems, once a page is overwritten, the previous content is lost unless proper versioning exists. This causes accidental deletions, confusion, and loss of important information.

The project solves this by providing:
1. A timeline of all saved versions
2. A visual comparison tool (diff viewer)
3. One-click restoration of older versions

4. Core Features

4.1 Must-Have Features
1. Automatically save a new version every time a user updates a page
2. Display a version timeline with timestamps and author names
3. Compare any two versions using Diff-Match-Patch
4. Restore or duplicate older versions

4.2 Stretch Goals
1. Additional editor features
2. Improved UI/UX
3. Performance enhancements

5. Tech Stack

5.1 Frontend
- HTML, CSS, JavaScript
- Tailwind CSS

5.2 Backend
- Django

5.3 Tools
- Diff-Match-Patch
- GitHub
- Postman

5.4 Deployment
- Render for frontend
- Replit for backend

6. System Flow
1. User logs into the CMS
2. User opens a page
3. System loads all previous versions
4. User selects two versions to compare
5. Differences are highlighted (added, removed, modified)
6. User restores a version if needed

7. Algorithms and Data Structures
1. Arrays and JSON objects for storing versions
2. Hash maps for quick metadata lookup
3. Diff-Match-Patch algorithm for generating differences

8. Testing Strategy
1. Unit testing for diff and restore functions
2. UI testing for version list and comparison screens
3. Performance testing for large documents

9. Project Timeline (4 Weeks)

Week 1: Requirements, database schema, API design  
Week 2: CRUD operations and diff logic  
Week 3: Version list UI and comparison UI  
Week 4: Testing, documentation, demo video  

10. Risks and Challenges
1. Accurately showing differences inside HTML content
2. Maintaining fast performance on large pages
3. Creating a scalable backend structure

11. Evaluation Requirements
We will submit:
1. Demo video
2. GitHub repository with documentation
3. Screenshots of version history and comparison

Success criteria:
1. Working CRUD and diff features
2. Accurate comparison outputs
3. Clean and responsive UI

12. Team Responsibilities

Backend: Aditya  
Diff Engine and Comparison: Puneet and Aditya  
Frontend UI: Puneet  
Integration and Testing: Puneet and Aditya  
Documentation and Demo Video: Aditya  

13. License
This project is open-source (MIT License recommended).
