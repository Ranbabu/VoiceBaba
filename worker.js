export default {
  async fetch(request) {
    const url = "https://your-app.onrender.com/tts";

    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        text: "नमस्कार दोस्तों"
      })
    });

    return new Response(response.body, {
      headers: {
        "Content-Type": "audio/wav"
      }
    });
  }
};
