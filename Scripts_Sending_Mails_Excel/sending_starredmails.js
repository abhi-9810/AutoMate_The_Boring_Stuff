function AddSM2GTDApp() {
      var threads = GmailApp.search('is:starred');
      for (var h = 0; h < threads.length; h++) {
        var messages = threads[h].getMessages();
        for (var i = 0; i < messages.length; i++) {
          if (messages[i].isStarred())
          {
            Logger.log(messages[i].getSubject());
            var subject = messages[i].getSubject();
            Logger.log(messages[i].getBody());
            var body = messages[i].getBody();
            Logger.log(messages[i].getId());
            var id = messages[i].getId();
            var label = GmailApp.getUserLabelByName("Add2GTDApp");
            threads[h].addLabel(label);
            messages[i].unstar();
            MailApp.sendEmail({
         to: "your@email.com",
         subject: subject,
         htmlBody: "https://mail.google.com/mail/u/0/#inbox/"+id+"<br>--------------------------------------------------------------------------------------<br>"+body+"<br>--------------------------------------------------------------------------------------<br>Mail to Nirvana Script ",
       }); 
          }
      }
    }
    }