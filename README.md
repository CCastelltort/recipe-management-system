# 🥘 Recipe Management System

This project is a **MySQL + Python** database system for a **Recipe Management System**. The system is designed to help users manage recipes, ingredients, dietary restrictions, and meal types, while supporting user-specific features like favorite recipes with ratings and comments. 

It includes:
- A MySQL schema with 9 tables.
- Preloaded data for users, recipes, ingredients, and more.
- A Python frontend (`front-end.py`) that interacts with the database via queries.


---

## 📁 Project Structure

- `schema.sql`: Contains all SQL commands to create the database.
- `populate_data.sql`: SQL commands to populate tables with initial data.
- `front-end.py`: Python script with an interactive CLI for querying and modifying the database.

---

## Features

- **User Accounts:** Users can register with a username and password.
- **Recipe Management:** Store recipes with names, descriptions, and associated ingredients.
- **Ingredient Tracking:** Maintain a list of ingredients with measurement units.
- **Dietary Restrictions:** Classify recipes based on dietary restrictions (e.g., gluten-free, vegan).
- **Cuisine and Meal Types:** Categorize recipes by cuisine type (Italian, Mexican, etc.) and meal type (appetizer, main course, dessert).
- **Favorites:** Users can mark recipes as favorites, add ratings, and leave comments.
- **Relational Integrity:** Foreign key constraints ensure consistency across tables.

---

## Database Tables Overview

| Table                | Purpose                                                       |
|----------------------|---------------------------------------------------------------|
| `users`              | Stores user details and credentials.                         |
| `recipe`             | Contains recipe information like name and description.      |
| `ingredient`         | Lists available ingredients and measurement units.          |
| `recipe_ingredients` | Maps recipes to ingredients with quantity.                   |
| `dietary_restriction`| Lists possible dietary restrictions.                         |
| `recipe_restriction` | Associates recipes with dietary restrictions.                |
| `cuisine`            | Links recipes to their cuisine type.                         |
| `meal_type`          | Associates recipes with meal types.                          |
| `favorite_recipe`    | Tracks users’ favorite recipes, ratings, and comments.      |

---
## Front-end Script (`front-end.py`)

This Python-based Command-Line Interface (CLI) connects to the MySQL database and enables interactive data operations, from simple data retrieval to modifications such as adding, updating, and deleting records.

### Features

- Retrieve usernames with User_Id below a specified value.
- List recipes with their ingredients.
- Show favorite recipes rated above average by a specific user.
- Display average ratings per cuisine.
- Add new recipes.
- Delete recipes above a certain Recipe_Id.
- Update User_Id values and cascade changes.
- Delete ingredients and cascade deletions.
