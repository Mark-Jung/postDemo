from models.JournalModel import JournalModel

class JournalController():

    @classmethod
    def new_journal(cls, data):
        # upload image to s3. returned with url
        url = "aws.com/hahahamarkjung"
        try:
            new_journal = JournalModel(data['title'], data['text'], data['longitude'],data['latitude'], url)
            new_journal.save_to_db()
        except Exception as e:
            print(e)
            return "Internal Server Error", 500, None

        return "", 201, None