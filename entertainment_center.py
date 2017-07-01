import media
import fresh_tomatoes

jurassic_park = media.Movie("Jurassic Park",
                            "http://img.moviepostershop.com/jurassic-park-movie-poster-1992-1020141477.jpg",
                            "https://www.youtube.com/watch?v=lc0UehYemQA")

the_godfather = media.Movie("The Godfather",
                            "https://images-na.ssl-images-amazon.com/images/I/31zYGA4NBpL.jpg",
                            "https://www.youtube.com/watch?v=5DO-nDW43Ik")
fight_club = media.Movie("Fight Club",
                         "http://www.posterbobs.com/images/fight_club3.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

inception = media.Movie("Inception",
                        "http://img.moviepostershop.com/inception-movie-poster-2010-1010547301.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

the_matrix = media.Movie("The Matrix",
                         "http://thebitplayers.net/wp-content/uploads/2015/08/the-matrix-movie-poster.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

memento = media.Movie("Memento",
                      "http://www.impawards.com/2001/posters/memento_xlg.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

# put movie instances into a list
movies = [jurassic_park, the_godfather, fight_club, inception, the_matrix, memento]

# render and open html page with passing the movie list
fresh_tomatoes.open_movies_page(movies)
