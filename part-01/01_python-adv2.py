""" Project: Social Media Scrapper """

from bs4 import BeautifulSoup
import csv

# load the html file
def load_html(file_path):
    with open(file_path, "r", encoding= "utf-8") as file:
        content = file.read()
    return content

# extract postss
def extract_post(soup):
    posts = []
    post_elements = soup.find_all("div", class_ = "post")
    for post in post_elements:
        username = post.find("h2", class_ = "username").text.strip()
        content = post.find("p", class_ = "content").text.strip()
        timestamp = post.find("span", class_ = "timestamp").text.strip()
        posts.append({"username": username, "content": content, "timestamp": timestamp})
    return posts

# save posts to csv file
def save_posts_to_csv(posts, output_path):
    with open(output_path, "w", newline= "", encoding= "utf-8") as file:
        writer = csv.DictWriter(file, fieldnames = ['username', 'content', 'timestamp'])
        writer.writeheader()
        writer.writerows(posts)

# main function
def main():
    print("Welcome to Social Media Scrapper")

    file_path = input("Enter the path of your social media's html file: ")
    html_content = load_html(file_path)
    soup = BeautifulSoup(html_content, "html.parser")
    posts =extract_post(soup)
    print("Extracted post successfully!")

    output_path = input("Enter the path to save csv file with .csv extension (eg. part-01/social_media_posts.csv)")
    save_posts_to_csv(posts, output_path)
    print("Posts saved to 'social_media_posts.csv' file!!")

if __name__ == "__main__":
    main()