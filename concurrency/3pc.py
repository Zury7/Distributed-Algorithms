import threading
import time
import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.state = "INITIAL"

    def can_commit(self):
        vote = random.choice(["YES", "NO"])
        print(f"[{self.name}] Vote: {vote}")
        return vote

    def pre_commit(self):
        self.state = "READY"
        print(f"[{self.name}] Pre-committing.")

    def do_commit(self):
        self.state = "COMMITTED"
        print(f"[{self.name}] Committing transaction.")

    def abort(self):
        self.state = "ABORTED"
        print(f"[{self.name}] Aborting transaction.")

class Coordinator:
    def __init__(self, participants):
        self.participants = participants

    def run_3pc(self):
        print("[Coordinator] Phase 1: CanCommit?")
        votes = []
        for p in self.participants:
            vote = p.can_commit()
            votes.append(vote)

        if all(v == "YES" for v in votes):
            print("[Coordinator] Phase 2: Sending Pre-Commit")
            for p in self.participants:
                p.pre_commit()
            time.sleep(1)  # Simulate waiting period

            print("[Coordinator] Phase 3: Sending Commit")
            for p in self.participants:
                p.do_commit()
        else:
            print("[Coordinator] Abort due to NO vote")
            for p in self.participants:
                p.abort()

if __name__ == "__main__":
    participants = [Participant(f"Participant-{i}") for i in range(3)]
    coordinator = Coordinator(participants)
    t = threading.Thread(target=coordinator.run_3pc)
    t.start()
    t.join()
