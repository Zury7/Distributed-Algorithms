import threading
import time
import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.vote = None

    def prepare(self):
        self.vote = random.choice(["YES", "NO"])
        print(f"[{self.name}] Vote: {self.vote}")
        return self.vote

    def commit(self):
        print(f"[{self.name}] Committing transaction.")

    def abort(self):
        print(f"[{self.name}] Aborting transaction.")

class Coordinator:
    def __init__(self, participants):
        self.participants = participants

    def run_2pc(self):
        print("[Coordinator] Phase 1: Sending prepare")
        votes = []
        for p in self.participants:
            vote = p.prepare()
            votes.append(vote)

        if all(v == "YES" for v in votes):
            print("[Coordinator] Phase 2: All voted YES. Sending commit.")
            for p in self.participants:
                p.commit()
        else:
            print("[Coordinator] Phase 2: At least one NO. Sending abort.")
            for p in self.participants:
                p.abort()

if __name__ == "__main__":
    participants = [Participant(f"Participant-{i}") for i in range(3)]
    coordinator = Coordinator(participants)
    t = threading.Thread(target=coordinator.run_2pc)
    t.start()
    t.join()
