# The-Perfect-Spiralator
A software tool to evaluate football throws using 2D pose estimation with OpenPose

Summary: The Perfect Spiral-ator is a video analysis tool that uses form estimation and computer vision techniques to scan through football tryout footage. The software evaluates players based on 3 criteria: form, ball trajectory, spin rate. The OpenPose 2D pose estimation algorithm was utilized to obtain the players joint coordinates for each throw in a video. From the joint coordinate data, we are able to assesses if the player body movement fulfills the good throw checklist (eg elbow of throwing arm is raised higher than shoulder level prior to ball release.)

More details can be found in this video: https://youtu.be/0-fDMyHvPFs

The image below demonstrates an example of how joint coordinates from video footage can be used to calculate if a player is throwing with good form

<img width="305" alt="image" src="https://user-images.githubusercontent.com/41973371/213006958-7c0c0286-17c3-4ccd-a027-be0d95123bc0.png">

Image description: A football player in shown midthrow with colored lines highlighting the locations of the joints as estimated by the openpose algorithm. The upper arm line (light orange) is the vector between the elbow and the shoulder while the shoulder line (red) is the vector between the shoulder and the neck. 

Form: The proper form for throwing a good spiral can be simplified into 4 main stages [3]: Late cocking phase: This phase involves the player pulling back their elbow before the throw. The elbow should be at shoulder height at the end of this phase.

Acceleration Phase: In this phase the player would want to ensure that the elbow and the wrist are moving in line as the wrist moves up and forward before the release of the ball. This phase ends when the ball is released.

Deceleration Phase: The ball should be released at the ideal incident angle for the desired distance. The wrist should snap down when the ball leaves the hand to maximize spin.

Follow through: The arm should come down and across the body toward the opposite hip. Proper follow through helps to avoid rapid deceleration and reduce force put on the shoulder.

Incident Angle: For a simple projectile, an incident angle of 45 degrees will achieve the maximum distance. However, the optimal incident angle will be lower for an object experiencing drag [9].

Spin rate: Players should try to achieve a spin rate of 600 rpm to maximize the benefits of gyroscopic motion and achieve the greatest distance [3].

