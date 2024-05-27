const { GoogleGenerativeAI } = require("@google/generative-ai");

async function singleRequest() {
  const genAI = new GoogleGenerativeAI(process.env.API_KEY);
 
  const model = genAI.getGenerativeModel({
    model: "gemini-pro",
  });
  const result = await model.generateContent({
    contents: [
      {
        role: "user",
        parts: [{ text: `Write a tech support email response for this question:

        "I can't use my emails and passwords in Chrome."` }],
      },
    ],
  });
  const response = await result.response;
  console.log(JSON.stringify(response));
}

singleRequest();
