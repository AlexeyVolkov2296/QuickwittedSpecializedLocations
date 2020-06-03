import requests

TOKEN = 'dae6a707c1eded9f9326e2b12aa0400eaacb2147dd1ebe1d1bd2ad2431eac9a669945d742d92edba3eba9'


class User:
    def __init__(self, user_id):
        self.USER_ID = user_id
        self.params = {
            'access_token': TOKEN,
            'v': 5.89,
            'user_id': self.USER_ID,
            'fields': 'nickname'
        }
    def __str__(self):
        return 'id=' + str(self.USER_ID)

    def get_friendlist(self):
        response = requests.get('https://api.vk.com/method/friends.get', params=self.params).json()
        id_set = set(i['id'] for i in response['response']['items'])
        return id_set

    def __and__(self, other_user):
        intersection = self.get_friendlist() & other_user.get_friendlist()
        common_list = []
        for id in intersection:
            common_list.append(User(id))
        return(common_list)



user1 = User(3647081)
user2 = User(15359702)



common = user1 & user2
for user in common:
    print(user)