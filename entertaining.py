import media
import  fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "BlaBla",
                        "https://goo.gl/images/vMYBup",
                        "https://www.youtube.com/watch?v=fOFgtfdRmw0")

avatar = media.Movie("Avatar",
                        "BlaBlaBla",
                        "https://goo.gl/images/jBLRmC",
                        "https://www.youtube.com/watch?v=_Tmz_ot3nnY")



# print (toy_story.storyline)
# avatar.show_trailer()
movies = [toy_story, avatar]

print (media.Movie.__name__)
# fresh_tomatoes.open_movies_page(movies)