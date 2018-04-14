from application.request_parser import SlackRequest


def answer_to_challenge(request):

    challege = request.find_from_request("challenge")

    if challenge:
        return challenge