/*

---general list of things we need to do-----
1. Make this scaleable to strings of messages, use NLP, etc
  a. TRY NOT TO RELY ON EVENT LISTENERS

---list of items we need to code ----
      -----core----
1. app.message needs to listen to everything <--- make it scalable as well
2. how do we detect spam?
  a. machine learning and neural networks <-- overkill imo
  b. natural langauge processing
  c. other scalable algorithm
3. Warning message as a courtesy - highly recommended.
4. Alert admins. That way they can audit the whole process and stuff.

    ---extensions and other fun things we can do
*/

//objects and instantiating
var spam_handle = require("./spam_handle.js");
var object = new spam_handle("hi");

//assinging slack signing secret and bot token
const { App } = require("@slack/bolt");
const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET
});

//message event
app.message("hi", async ({ payload, context }) => {
  try {
    const result = await app.client.chat.postMessage({
      token: context.botToken,
      channel: payload.channel,
      text: object.response
    });
    console.log(result);
  } catch (error) {
    console.error(error);
  }
});

//async function
(async () => {
  // starts the app
  await app.start(process.env.PORT || 3000);
  console.log("⚡️ Bolt app is running!");
})();
