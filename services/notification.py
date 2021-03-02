'''
    [Amazon Simple Notification Service(SNS) with Google Firebase Cloud Messaging(FCM)]
    How user notifications work

    You send push notification messages to both mobile devices and desktops using one of the following supported push notification services:

    Amazon Device Messaging (ADM)
    Apple Push Notification Service (APNs) for both iOS and Mac OS X
    Baidu Cloud Push (Baidu)
    Firebase Cloud Messaging (FCM)
    Microsoft Push Notification Service for Windows Phone (MPNS)
    Windows Push Notification Services (WNS)

    User notification process overview

    Obtain the credentials and device token for the mobile platforms that you want to support.
    Use the credentials to create a platform application object (PlatformApplicationArn) using Amazon SNS. For more information, see Creating a platform endpoint.
    Use the returned credentials to request a device token for your mobile app and device from the mobile platforms. The token you receive represents your mobile app and device.
    Use the device token and the PlatformApplicationArn to create a platform endpoint object (EndpointArn) using Amazon SNS. For more information, see Creating a platform endpoint.
    Use the EndpointArn to publish a message to an app on a mobile device. For more information, see Publishing to a mobile device and the Publish API in the Amazon Simple Notification Service API Reference.
'''
