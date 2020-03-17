from hicalweb.judgment.models import Judgement
from hicalweb.progress.models import Task

def load_all_documents():
    import json
    with open('all_documents_to_judge.json', 'r') as f:
        return json.load(f)

ALL_DOCUMENTS = load_all_documents()

def get_document(docid):
    for docs in ALL_DOCUMENTS.values():
        for doc in docs:
            if doc['doc_id'] == docid:
                return [doc]
    raise ValueError('Could not find doc')

def get_documents(topic):
    tasks_for_topic = [i for i in Task.objects.filter(topic=topic)]
    print(tasks_for_topic)
    judgments_for_topic = set([i.doc_id for i in Judgement.objects.filter(task__in = tasks_for_topic)])
    print(judgments_for_topic)

    return [i for i in ALL_DOCUMENTS[str(topic.id)] if i['doc_id']  not in judgments_for_topic]

