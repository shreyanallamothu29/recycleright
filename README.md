<h1>♻️ RecyleRight</h1>
<h2>The Issue</h2>
<p>This is my dad! Like most parents, he doesn’t like to waste. Growing up, I noticed how much effort he went through to research how to properly dispose of everyday items like pizza boxes and plastic bags. And he’s not alone.</p>
<p>A 2025 survey from <a href="https://kab.org/americans-overwhelmingly-support-recycling-yet-rates-remain-stubbornly-low-and-many-dont-get-it-right/">The Harris Poll</a> found that while nearly 90% of Americans think that recycling is important, household recycling rates remain at just 32%—largely due to confusion around proper recycling practices. For example, many people don’t know that pizza boxes with grease can’t be recycled, or that plastic bags cannot be recycled curbside.</p>
<p>I created RecycleRight to help not just my dad, but everyone who wants to recycle correctly without the confusion or endless Googling.</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/shreyanallamothu29/recycleright/a307f2f8b0a8c51583b9cae76b352ac5b7269892/me_and_dad.JPG" width="300">
</p>

<h2>My Solution</h2>

<p>Simply upload a photo of an item you’re unsure how to recycle, and RecycleRight will tell you whether it’s recyclable and how to dispose of it properly. Then, enter your zip code to get a list of nearby drop-off locations and facilities.</p>
<p>RecycleRight provides relevant, location-based information for everything from batteries to clothing to household food waste.</p>

<h2>Impact</h2>
<p>Serving on my town’s Youth Council was another catalyst for creating RecycleRight. As a delegate, I got to conduct firsthand user research while touring local waste management and recycling facilities and observing how the system operates in practice. For example, I learned that when items are mis-sorted, facility workers have to painstakingly manually remove them, which slows processing and increases costs. Since then, RecycleRight has been adopted by the Town of Normal and McLean County Ecology Action Center!</p>

<h2>The Process</h2>
<p>This was my first time training a machine learning model in PyTorch. I compiled and labeled a custom dataset of common household items and fine-tuned a ResNet50 convolutional neural network to classify images of recyclables into disposal categories. It was rough at first…</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/shreyanallamothu/recycleright/refs/heads/main/test_loss_before.png" width="400">
</p>
<p>But after many (many) batches and experimenting with hyperparameters like preprocessing and training step sizes, I got my model up to 95% testing accuracy!</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/shreyanallamothu29/recycleright/refs/heads/main/test_loss_after.png" width="400">

</p>
<h2 align="center"><a href="https://colab.research.google.com/drive/1IqD-ngqcYkEJMWfcPY-8Dw-iM2NmMWXk?usp=sharing" style="color: blue">View my Colab Notebook and PyTorch Model!</a></h2>

<p>The most challenging part of building RecycleRight was learning how to integrate the front and back end Flask, since this was my first time deploying a full-stack ML application. I used Flask to integrate the model with a clean, beautiful front end. My goal was to make the page as intuitive as possible to encourage everyday use!</p>

<h2>What’s Next</h2>
<p>I hope to deploy RecycleRight as an app and expand the dataset to cover more types of plastic in greater detail.</p>
