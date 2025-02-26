class User:
  def __init__(self, username, bio=""):
    self.username = username
    self.bio = bio
    self.friends = [] 
    self.posts = [] 

  def add_friend(self, friend):
    if friend not in self.friends:
      self.friends.append(friend) 
      print(f"{friend.username} added to your friends list!")
    else:
      print(f"{friend.username} is already your friend.")

  def post_update(self,content):
    new_post = Post(content, self.username)
    self.posts.append(new_post)
    print("Your post has been published!") 

  def view_profile(self):
    print(f"\n--- {self.username}'s Profile ---")
    print(f"Bio: {self.bio}")
    print("\nFriends:")
    for friend in self.friends:
      print(f"- {friend.username}")
    print("\nPosts:")
    for post in self.posts:
      print(f"- {post.content} (Posted on: {post.timestamp})")

class Post:
  def __init__(self, content, author):
    from datetime import datetime 
    self.content = content 
    self.author = author 
    self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class SocialNetwork:
  def __init__(self):
    self.users = {} 

  def create_user(self, username, bio=""):
    if username in self.users:
      print("Username already exists! Try another one.") 
    else:
      new_user = User(username, bio)
      self.users[username] = new_user 
      print(f"User '{username}' creaetd successfully!")
      
  def get_user(self, username):
    return self.users.get(username) 

  def display_menu(self):
    print("\n--- Social Networking App ---") 
    print("1. Create Profile")
    print("2. Add Friend")
    print("3. View Friends") 
    print("4. Post Update")
    print("5. View Profile") 
    print("6. Exit") 

# Main Program
def main():
  network = SocialNetwork()
  while True:
    network.display_menu() 
    choice = input("Enter your choice (1-6): ")
    if choice == "1":  # Create Profile
      username = input("Ener a username: ")
      bio = input("Enter a short bio (optional): ") 
      network.create_user(username, bio) 
    elif choice == "2":  # Add friend 
      username = input("Enter your username: ")
      user = network.get_user(username)
      if user:
        friend_username = input("Enter your friend's username: ") 
        friend = network.get_user(friend_username) 
        if friend:
          user.add_friend(friend)
        else:
          print("Friend not found.")
      else:
        print("User not found.")
    elif choice == "3": # View Friends
      username = input("Enter your username: ") 
      user = network.get_user(username) 
      if user:
        print("\n Your Friends:")
        for friend in user.friends:
          print(f"- {friend.username}")
      else:
        print("User not found.")
    elif choice == "4": # Post Update
      username = input("Enter your username: ")
      user = network.get_user(username)
      if user:
        content = input("Write your post: ")
        user.post_update(content)
      else:
        print("User not found.")
    elif choice == "5":  # View Profile 
      username = input("Enter your username: ")
      user = network.get_user(username) 
      if user:
        user.view_profile() 
      else:
        print("User not found.")
    elif choice == "6": # Exit 
      print("Goodbye! Thanks for using the Social Networking App.") 
      break
  else:
    print("Inalid chocie. Please try again.")
      

# Run the program
if __name__ == "__main__":
  main()

      
      
        
      
      


    







  
