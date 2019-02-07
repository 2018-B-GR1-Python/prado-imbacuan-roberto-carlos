import facebook

page_tokem = 'EAAdVlZBsithsBAFFwxEOkiBUSDRq82HUIMOoUGxQuUsS48n3UgLFWz70Vbf3gUdkTelZBSf4Y7jetdXZAuYy2pNYCng2iuzI6Kcj0InDX6s12GF99IjwJdqic1KDu00psuYcUzbU3Fxh20a7ZAxfV2ZBLKm0yiZBdzYLuEDQLZC9BRhC6UVVAK7dbaJ3sHFtnXhUmQwVzoV7cravsaNCHeaJ0ZAta3NZBnqafOiiVWpgyGwZDZD'

graph = facebook.GraphAPI(access_token=page_tokem, version="2.12")

id = "1999532883506746"

feed = graph.get_object(id=id, fields='feed')
posts = feed['feed']['data']
for post in posts:
    print('\n')
    print(f"ID: {post['id']}")
    print(f"Content: {post['message']}")

    id_post = post['id']
    comments = graph.get_object(id=id_post, fields='comments')
    comments_data = comments['comments']['data']
    print('Comentarios:')
    for comment in comments_data:
        print(f"{comment['from']['name']}: {comment['message']}")

    likes = graph.get_object(id=id_post, fields='likes.limit(1).summary(true)')
    print(f"Likes: {likes['likes']['summary']['total_count']}")

    general = graph.get_object(id=id_post, fields='comments, likes.limit(1).summary(true)')
    print(general)

