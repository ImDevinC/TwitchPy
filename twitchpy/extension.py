class Extension:
    """
    Represents an extension
    """

    def __init__(self,author_name,bits_enabled,can_install,configuration_location,description,eula_tos_url,has_chat_support,icon_url,icon_urls,id,name,privacy_policy_url,request_identity_link,screenshot_urls,state,subscriptions_support_level,summary,support_email,version,viewer_summary,views,allowlisted_config_urls,allowlisted_panel_urls):
        """
        Args:
            author_name (str): Name of the individual or organization that owns the Extension
            bits_enabled (bool): Whether the Extension has features that use Bits
            can_install (bool): Indicates if a user can install the Extension on their channel
                                They may not be allowed if the Extension is currently in testing mode and the user is not on the allow list
            configuration_location (str): Whether the Extension configuration is hosted by the EBS or the Extensions Configuration Service
            description (str): The description of the Extension
            eula_tos_url (str): URL to the Extension’s Terms of Service
            has_chat_support (bool): Indicates if the Extension can communicate with the installed channel’s chat
            icon_url (str): The default icon to be displayed in the Extensions directory
            icon_urls (dict): The default icon in a variety of sizes
            id (str): The autogenerated ID of the Extension
            name (str): The name of the Extension
            privacy_policy_url (str): URL to the Extension’s privacy policy
            request_identity_link (bool): Indicates if the Extension wants to explicitly ask viewers to link their Twitch identity
            screenshot_urls (list): Screenshots to be shown in the Extensions marketplace
            state (str): The current state of the Extension
                         Valid values are "InTest", "InReview", "Rejected", "Approved", "Released", "Deprecated", "PendingAction", "AssetsUploaded", "Deleted"
            subscriptions_support_level (str): Indicates if the Extension can determine a user’s subscription level on the channel the Extension is installed on
            summary (str): A brief description of the Extension
            support_email (str): The email users can use to receive Extension support
            version (str): The version of the Extension
            viewer_summary (str): A brief description displayed on the channel to explain how the Extension works
            views (dict): All configurations related to views such as: mobile, panel, video_overlay, and component
            allowlisted_config_urls (list): Allow-listed configuration URLs for displaying the Extension
            allowlisted_panel_urls (list): Allow-listed panel URLs for displaying the Extension
        """

        self.author_name=author_name
        self.bits_enabled=bits_enabled
        self.can_install=can_install
        self.configuration_location=configuration_location
        self.description=description
        self.eula_tos_url=eula_tos_url
        self.has_chat_support=has_chat_support
        self.icon_url=icon_url
        self.icon_urls=icon_urls
        self.id=id
        self.name=name
        self.privacy_policy_url=privacy_policy_url
        self.request_identity_link=request_identity_link
        self.screenshot_urls=screenshot_urls
        self.state=state
        self.subscriptions_support_level=subscriptions_support_level
        self.summary=summary
        self.support_email=support_email
        self.version=version
        self.viewer_summary=viewer_summary
        self.views=views
        self.allowlisted_config_urls=allowlisted_config_urls
        self.allowlisted_panel_urls=allowlisted_panel_urls