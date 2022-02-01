# -*- coding: UTF-8 -*-

from fbchat import log, Client
import sample


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        #___
        sch = message_object.text
        sd = sch.lower().rstrip()
        if sd == "monday":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\11.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "cat":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\cat.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "dog":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\dog.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "gir":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\123.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "tuesday":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\22.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "wednesday":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\33.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "thursday":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\44.png', thread_id=thread_id, thread_type=thread_type)
            return
        elif sd == "friday":
            client.sendLocalImage(r'E:\Програмування\fbchat\examples\55.png', thread_id=thread_id, thread_type=thread_type)
            return

        samp = sample.read_sample(r"E:\Програмування\fbchat\examples\vybir.txt")
        message_object.text = sample.find_answer(message_object.text.lower(), samp)

        #___
        #print(message_object.text)

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)


client = EchoBot("faryna562pavlo@gmail.com", "killer4321")
client.listen()
