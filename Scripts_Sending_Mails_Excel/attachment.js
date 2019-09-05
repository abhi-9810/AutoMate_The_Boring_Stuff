// This code fetches the Google and YouTube logos, inlines them in an email
 // and sends the email
 function inlineImage() {
   var googleLogoUrl = "http://www.google.com/intl/en_com/images/srpr/logo3w.png";
   var youtubeLogoUrl =
         "https://developers.google.com/youtube/images/YouTube_logo_standard_white.png";
   var googleLogoBlob = UrlFetchApp
                          .fetch(googleLogoUrl)
                          .getBlob()
                          .setName("googleLogoBlob");
   var youtubeLogoBlob = UrlFetchApp
                           .fetch(youtubeLogoUrl)
                           .getBlob()
                           .setName("youtubeLogoBlob");
   MailApp.sendEmail({
     to: "recipient@example.com",
     subject: "Logos",
     htmlBody: "inline Google Logo<img src='cid:googleLogo'> images! <br>" +
               "inline YouTube Logo <img src='cid:youtubeLogo'>",
     inlineImages:
       {
         googleLogo: googleLogoBlob,
         youtubeLogo: youtubeLogoBlob
       }
   });
 }
