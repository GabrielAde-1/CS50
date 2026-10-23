#### Celebration Wishlist Tracker

#### A Web-based Gift Registry Management Solution

**Author:** Gabriel Adejugbe

**GitHub Username:** GabrielAde-1

**edX Username:** adejugbegabriel

**Location:** Walsall, UK

**Date:** 23/10/26 

#### Project Video Walkthrough

* **Video URL:** https://www.youtube.com/watch?v=GuPVK96SGq4

#### Detailed Project Overview

The Celebration Wishlist Tracker is a responsive web application built using Python, Flask, and SQLite. The primary goal of this application is to solve a common, practical everyday problem: keeping track of specific gift concepts, desires, and registries for friends and family members across various holiday milestones throughout the year. Often, people mention specific items they want in passing conversation, only for those ideas to be forgotten by the time a birthday, graduation, or holiday season arrives. This web application bridges that gap by providing a central digital ledger where a user can rapidly log, track, and clear gift ideas on demand. 

While conceptually inspired by the structures explored within the dynamic database problems of CS50x (specifically the Week 9 Birthdays problem set), this implementation completely overhauls the structural presentation, user experience, data validation handling, and capabilities. It shifts away from tracking a static calendar constraint like dates of birth toward processing multi-variable textual descriptors (Item Names and Occasions). Furthermore, this project incorporates full relational state destruction mechanics through asynchronous form manipulation routing, enabling users to clear out completed entries natively within the interface layout. 

#### Architectural Structure and Design Choices

The application layout strictly follows the traditional Model-View-Controller architectural blueprint natively promoted by the Flask microframework. This approach guarantees clean separation of concerns across structural styles, state modifications, and database lookups. 

Below is an examination of the files comprising the system core: 

#### 1. Backend Application Controller (app.py)

The Python backend engine serves as the main gateway routing requests throughout the workspace. It initializes the Flask context server, dynamically updates environment parameter flags to auto-reload template changes during active development workflows, and handles database connection persistence via the CS50 SQL wrapper object. 

The backend exposes two programmatic interface endpoints: 

* **@app.route("/", methods=["GET", "POST"])**: The central index route handles multi-method requests. When a user navigates to the page (GET request), the engine executes an explicit structured search query on the SQLite database file to draw up every recorded wishlist row entry. These values are packaged and forwarded into the Jinja template compiler wrapper engine. When a web form payload lands on the index via a submission (POST request), the backend strips the parameter keys out of the HTTP request payload dictionary context. It checks the fields to prevent empty database writes, then drops them safely into the SQLite row schemas via a parameterized injection-safe query syntax structure.
* **@app.route("/delete", methods=["POST"])**: This endpoint provides management handling by listening specifically for target ID flags. When triggered, it executes a precise database deletion command to remove the targeted data row before seamlessly refreshing the viewport screen layout.

#### 2. Layout Wrapper Configuration (templates/layout.html)

To minimize markup duplication and keep structural updates clean, the application utilizes Jinja layout inheritance protocols. The base architecture file sets up essential document tags, loads typography layers straight from external CDNs, links the visual engine stylesheet files, and establishes a prominent structural banner header panel. The actual dynamic body items are systematically compiled using clean container blocks. 

#### 3. Visual Grid View Document (templates/index.html)

The index page structures data into two cleanly divided workspace grid components. The top segment implements an explicit interactive interface containing target attribute capture elements. Native HTML validation parameters work alongside backend checks to ensure users cannot submit partial records. The lower portion dynamically unrolls raw table data loops via sequential Jinja templating operations. If the internal array variable structure registers as empty, the layout safely bypasses structural rendering loops cleanly without throwing critical compilation faults. 

#### 4. Component Stylesheet Layout (static/styles.css)

Moving completely clear of traditional Bootstrap framework dependencies, the stylesheet interface layer uses custom vanilla CSS layout rules. The interface relies on CSS Flexbox frameworks alongside specific CSS variables to layout cards cleanly. It applies a modern gradient layout across standard container margins, includes focus state highlight transitions to prompt input validation tracking, and integrates specific color-coded delete link element items to prevent layout confusion during high-speed desktop use cases. 

#### 5. Persistent Data Store Ledger (wishlist.db)

The underlying data layer utilizes an embedded transactional relational storage table pattern configured strictly using lightweight SQLite query syntax rules. The table architecture consists of four distinct columns: 

* id: An integer primary key tracking increment counters sequentially to keep tracking pointers safe.
* name: A variable-length character text grid mapping the recipient's target name data.
* item: A description storage field containing target object registry keywords.
* event: An identifier column organizing the milestone occasion types across historical markers.

#### Installation, Deployment, and Launch Sequence

Getting the script up and running locally inside your secure CS50 development sandbox workspace environment is designed to be as fast as possible. Follow this sequence exactly: 

1. **Verify Your Location Context**: Use your workspace terminal window to ensure you are sitting cleanly inside the root folder mapping: 

bash

cd wishlist_tracker

Use code with caution.
2. **Review Environment Components**: Ensure that all critical application code pieces are sitting in their correct structural tracks (app.py in the root, matching view components resting straight inside /templates and /static).
3. **Spin Up the Server Gateway**: Boot up the development engine layer by instructing the global Python system daemon to launch your Flask application wrapper framework natively: 

bash

flask run

Use code with caution.
4. **Access the Viewport Link**: Command-click or follow the automatically provisioned virtual port gateway link output directly within your terminal window interface dashboard to load the web tracker in an active browser tab.
