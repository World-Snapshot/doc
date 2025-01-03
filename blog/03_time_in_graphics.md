# Time Flowing in Graphics

## The Arrow Paradox

As we all know, space-time is one of the cornerstones of world existence, so understanding space-time is an essential condition for exploring the mysteries of the world. The ancient Greek philosopher Zeno proposed several [famous paradoxes](https://en.wikipedia.org/wiki/Zeno%27s_paradoxes), and we'll use the Arrow Paradox as an example:

A flying arrow, in the smallest unit of space-time, appears forever stationary to the observer. In it, space-time exhibits discontinuous properties. If we take snapshots of its flight process and divide them infinitely, the arrow is always stationary.

The problem with this paradox lies in the fact that the motion of "flight" depends on two points in time. That is, whether the arrow moves from this moment to that moment. This involves the form of existence of space-time: is space-time continuous, like concepts, or discontinuous, like matter? The results this brings are completely different.

These methods can be explained by the concept of calculus (infinity), but still cannot be solved by calculus, because the premise of calculus principles is the existence of extension (for example, a line segment with extension after infinite division is still composed of line segments with extension, rather than points without extension), while Zeno's paradox both acknowledges extension and emphasizes points without extension.

## Space-time in Reality and Vision

Modern physics has given us the answer. [Planck time](https://en.wikipedia.org/wiki/Planck_units#Planck_time) is the shortest time scale in physics, and [Planck length](https://en.wikipedia.org/wiki/Planck_units#Planck_length) is the shortest distance scale. Space-time is discontinuous, and there is nothing shorter than these two scales.

The World Snapshot Model generates videos composed of countless world frames. Ordinary videos generally have 24 or thirty frames per second, and the real world can be seen as an ideal WSV video with 1/Planck time (frame rate approximately 1.855 x 10^43). World Snapshot can theoretically infinitely approach the frame rate of the real world, although it falls far short in practical applications.

However, in design, we should try to consider how World Snapshot combines with real properties, as they are so similar even in their smallest discontinuities.

## Infusing Time Properties into Graphics

When we see a video clip, we can see the creation and editing dates of the video. But when these properties are stripped away, and only different frames are trained, the model at most knows that this is the nth frame out of m frames.
This is somewhat crude, because humans can know that a news video happened in 1999, lasted for 1 hour, while another scene happened in 2001, for two hours. This helps us understand the world.

For example, when the model is training, it might see the Titanic hitting an iceberg, and in another video judgment, it sees the Titanic setting sail. But to it, it would think these two events are not strongly related. Therefore, we should not only try to utilize the video's timestamp but also try to add relative time to each frame.

Moreover, when we train, we can consider using the midpoint of each video, letting the model know what is the relative future and past. This way, we can give the model the concept of "past." Just as I think models are two-dimensional beings, the vast majority of generative models don't have the concept of "past" at all.

*Conceived this blog on 24 Dec 24, Completed on 3th Jan 25*