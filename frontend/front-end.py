import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host = "",
        user = "",
        password = "",
        database = "" 
        )

#LEVEL 1: Query 1
def get_usernames_with_id_below_5(db_connection):
    """
    Selects all the usernames of the users that have a User_Id number smaller than 5.

    """
    query = "SELECT Username FROM users WHERE User_Id < 5;"
    with db_connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nUsernames with User_Id below 5:")
        for row in results:
            print(row[0])

#LEVEL 1: Query 2
def get_recipe_and_ingredients_of_recipeId(db_connection):
    """
    Selects the recipe name and ingredient names for a specified recipe ID.
    Accepts user input to specify the Recipe_Id.
    If a Recipe_Id is not specified, it takes 33 as default.

    """
    try:
        recipe_id = int(input("Enter Recipe_Id (default: 33): ") or 33)
    except ValueError:
        print("Invalid input. Using default Recipe_Id = 33.")
        recipe_id = 33
    query = """
    SELECT r.Name AS recipe_name, i.Ingredient_Name AS ingredient_name
    FROM recipe r
    JOIN recipe_ingredients ri ON r.Recipe_Id = ri.Recipe_id
    JOIN ingredient i ON ri.Ingredient_Id = i.Ingredient_Id
    WHERE r.Recipe_Id = %s;
    """
    with db_connection.cursor() as cursor:
        cursor.execute(query, (recipe_id,))
        results = cursor.fetchall()
        print(f"\nIngredients for Recipe_Id {recipe_id}:")
        for row in results:
            print(f"{row[0]} - {row[1]}")

#LEVEL 1: Query 3
def get_favorite_recipes_with_ratings_above_avg(db_connection):
    """
    Selects recipes that a specific user has favorited and rated above the average rating of all the rating of all the users favorite recipes.
    Accepts user input for the User_Id.
    If a User_Id is not specified, it takes 1 as default.

    """
    user_id = input("Enter User_Id (default: 1): ") or "1"
    query = f"""
    SELECT r.Name
    FROM recipe r
    JOIN favorite_recipe fr ON r.Recipe_Id = fr.Recipe_Id
    WHERE fr.User_Id = {user_id} AND fr.rating > (
        SELECT AVG(rating) FROM favorite_recipe
    );
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"\nFavorite recipes with ratings above average for User_Id {user_id}:")
    for row in results:
        print(row[0])
    cursor.close()

#LEVEL 1: Query 4
def get_avg_rating_per_cuisine(db_connection):
    """
    Selects cuisine names and their average rating.

    """
    query = """
    SELECT c.Cuisine_Name, AVG(fr.rating)
    FROM favorite_recipe fr
    JOIN cuisine c ON c.Recipe_Id = fr.Recipe_Id
    GROUP BY c.Cuisine_Name;
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nAverage rating per cuisine:")
    for row in results:
        print(f"{row[0]}: {row[1]:.2f}")
    cursor.close()

#LEVEL 2: Query 1
def add_recipe(db_connection):
    """
    Adds a new recipe to the recipe table.
    Accepts user input for the recipe name and description.

    """
    name = input("Enter recipe name: ")
    description = input("Enter recipe description: ")
    query = "INSERT INTO recipe (Name, Description) VALUES (%s, %s);"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, description))
    db_connection.commit()
    print("Recipe added successfully.")
    cursor.close()

#LEVEL 2: Query 2
def delete_recipes_above_recipeId(db_connection):
    """
    Deletes recipes from the recipe table where Recipe_Id is bigger than the specified value.
    Accepts user input for the maximum Recipe_Id to keep.
    If a Recipe_Id is not specified, it takes 50 as default.

    """
    recipe_id = input("Enter the maximum Recipe_Id to keep (default: 50): ") or "50"
    query = f"DELETE FROM recipe WHERE Recipe_Id > {recipe_id};"
    cursor = db_connection.cursor()
    cursor.execute(query)
    db_connection.commit()
    print(f"Recipes with Recipe_Id greater than {recipe_id} deleted successfully.")
    cursor.close()

#LEVEL 2: Query 3
def update_userId(db_connection):
    """
    Updates User_Id and cascades the change to related tables.
    Accepts user input for old and new User_Id.
    If a old User_Id is not specified, it takes 50 as default.
    If new User_Id is not specified, it takes 51 as default.

    """
    old_user_id = input("Enter the old User_Id (default: 50): ") or "50"
    new_user_id = input("Enter the new User_Id (default: 51): ") or "51"
    query = f"UPDATE users SET User_Id = {new_user_id} WHERE User_Id = {old_user_id};"
    cursor = db_connection.cursor()
    cursor.execute(query)
    db_connection.commit()
    print(f"User_Id updated from {old_user_id} to {new_user_id} successfully.")
    cursor.close()

#LEVEL 2: Query 4
def delete_ingredient(db_connection):
    """
    Deletes an ingredient and cascades deletion to related tables.
    Accepts user input for the Ingredient_Id to delete.
    If Ingredient_Id is not specified, it takes 1 as default

    """
    ingredient_id = input("Enter the Ingredient_Id to delete (default: 1): ") or "1"
    query = f"DELETE FROM ingredient WHERE Ingredient_Id = {ingredient_id};"
    cursor = db_connection.cursor()
    cursor.execute(query)
    db_connection.commit()
    print(f"Ingredient with Ingredient_Id {ingredient_id} deleted successfully.")
    cursor.close()



def main():
    db_connection = get_db_connection()
    try:
        while True:
            print("\nChoose a query to execute:")
            print("1. Get usernames with User_Id below 5")
            print("2. Get recipe and ingredients for a specific recipe")
            print("3. Get favorite recipes with ratings above average")
            print("4. Get average rating per cuisine")
            print("5. Add a new recipe")
            print("6. Delete recipes with Recipe_Id > specified value")
            print("7. Update User_Id")
            print("8. Delete ingredient")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                get_usernames_with_id_below_5(db_connection)
            elif choice == "2":
                get_recipe_and_ingredients_of_recipeId(db_connection)
            elif choice == "3":
                get_favorite_recipes_with_ratings_above_avg(db_connection)
            elif choice == "4":
                get_avg_rating_per_cuisine(db_connection)
            elif choice == "5":
                add_recipe(db_connection)
            elif choice == "6":
                delete_recipes_above_recipeId(db_connection)
            elif choice == "7":
                update_userId(db_connection)
            elif choice == "8":
                delete_ingredient(db_connection)
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
    finally:
        db_connection.close()

if __name__ == "__main__":
    main()
