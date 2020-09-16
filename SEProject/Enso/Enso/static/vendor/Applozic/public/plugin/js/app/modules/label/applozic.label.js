var mckLabels = new MckLabels();
function MckLabels() {
    var _this = this;

    _this.getLabels = function() {
        return  {
            'conversations.title': 'Conversations',
            'start.new': 'Start New',
            'search.contacts': 'Contacts',
            'search.groups': 'Groups',
            'empty.groups': 'No groups yet!',
            'empty.contacts': 'No contacts yet!',
            'empty.messages': 'No messages yet!',
            'no.more.messages': 'No more messages!',
            'empty.conversations': 'No conversations yet!',
            'no.more.conversations': 'No more conversations!',
            'search.placeholder': 'Search...',
            'location.placeholder': 'Enter a location',
            'create.group.title': 'Create Group',
            'members.title': 'Members',
            'add.members.title': 'Add Member',
            'remove.member': 'Remove Member',
            'change.role': 'Change Role',
            'group.info.update': 'Update',
            'group.info.updating': 'Updating...',
            'add.group.icon': 'Add Group Icon',
            'group.deleted': 'Group has been deleted',
            'change.group.icon': 'Change Group Icon',
            'group.title': 'Group Title',
            'group.type': 'Group Type',
            'group.create.submit': 'Creating Group...',
            'blocked': 'You have blocked this user',
            'group.chat.disabled': 'You are no longer part of this group!',
            'block.user.alert': 'Are you sure you want to block this user?',
            'unblock.user.alert': 'Are you sure you want to unblock this user?',
            'exit.group.alert': 'Are you sure you want to exit this group?',
            'remove.member.alert': 'Are you sure you want to remove this member?',
            'clear.messages.alert': 'Are you sure you want to delete all the conversation?',
            'typing': 'typing...',
            'is.typing': 'is typing...',
            'online': 'Online',
            'clear.messages': 'Clear Messages',
            'delete': 'Delete',
            'reply': 'Reply',
            'forward': 'Forward',
            'copy': 'Copy',
            'block.user': 'Block User',
            'unblock.user': 'Unblock User',
            'group.info.title': 'Group Info',
            'exit.group': 'Exit Group',
            'location.share.title': 'Location Sharing',
            'my.location': 'My Location',
            'send': 'Send',
            'send.message': 'Send Message',
            'smiley': 'Smiley',
            'close': 'Close',
            'edit': 'Edit',
            'save': 'Save',
            'file.attachment': 'Files & Photos',
            'file.attach.title': 'Attach File',
            'last.seen': 'Last seen',
            'last.seen.on': 'Last seen on',
            'hour':' hour',
            'min':' min',
            'yesterday':'yesterday',
            'hours':' hours',
            'mins':' mins',
            'time.format.AM':'AM',
            'time.format.PM':'PM',
            'time.format.am':'am',
            'time.format.pm':'pm',
            'user.delete':'This user has been deleted',
            'ago': 'ago',
            'admin':'Admin',
            'user':'User',
            'moderator':'Moderator',
            'member':'Member',
            'public':'Public',
            'private':'Private',
            'open':'Open',
            'you':'You',
            'userIdPattern':'[^!$%\^&*()]+',
            'charsNotAllowedMessage':'Following characters are not allowed: !$%^&*()',
            'group.metadata': {
                'CREATE_GROUP_MESSAGE': ':adminName created group :groupName',
                'REMOVE_MEMBER_MESSAGE': ':adminName removed :userName',
                'ADD_MEMBER_MESSAGE': ':adminName added :userName',
                'JOIN_MEMBER_MESSAGE': ':userName joined',
                'GROUP_NAME_CHANGE_MESSAGE': 'Group name changed to :groupName',
                'GROUP_ICON_CHANGE_MESSAGE': 'Group icon changed',
                'GROUP_LEFT_MESSAGE': ':userName left',
                'DELETED_GROUP_MESSAGE': ':adminName deleted group',
                'GROUP_USER_ROLE_UPDATED_MESSAGE': ':userName is :role now',
                'GROUP_META_DATA_UPDATED_MESSAGE': '',
                'ALERT': '',
                'HIDE': ''
            }
        };  
    }

    _this.setLabels = function() {
        $applozic('#mck-conversation-title').html(MCK_LABELS['conversations.title']).attr('title', MCK_LABELS['conversations.title']);
        $applozic('#mck-msg-new, #mck-sidebox-search .mck-box-title').html(MCK_LABELS['start.new']).attr('title', MCK_LABELS['start.new']);
        $applozic('#mck-contact-search-tab strong').html(MCK_LABELS['search.contacts']).attr('title', MCK_LABELS['search.contacts']);
        $applozic('#mck-group-search-tab strong').html(MCK_LABELS['search.groups']).attr('title', MCK_LABELS['search.groups']);
        $applozic('#mck-contact-search-input, #mck-group-search-input, #mck-group-member-search').attr('placeholder', MCK_LABELS['search.placeholder']);
        $applozic('#mck-loc-address').attr('placeholder', MCK_LABELS['location.placeholder']);
        $applozic('#mck-no-conversations').html(MCK_LABELS['empty.conversations']);
        $applozic('#mck-no-messages').html(MCK_LABELS['empty.messages']);
        $applozic('#mck-no-more-conversations').html(MCK_LABELS['no.more.conversations']);
        $applozic('#mck-no-more-messages').html(MCK_LABELS['no.more.messages']);
        $applozic('#mck-no-search-contacts').html(MCK_LABELS['empty.contacts']);
        $applozic('#mck-no-search-groups').html(MCK_LABELS['empty.groups']);
        $applozic('#mck-new-group, #mck-group-create-tab .mck-box-title, #mck-btn-group-create').html(MCK_LABELS['create.group.title']).attr('title', MCK_LABELS['create.group.title']);
        $applozic('#mck-gc-overlay-label').html(MCK_LABELS['add.group.icon']);
        $applozic('#mck-msg-error').html(MCK_LABELS['group.deleted']);
        $applozic('#mck-gc-title-label').html(MCK_LABELS['group.title']);
        $applozic('#mck-gc-type-label').html(MCK_LABELS['group.type']);
        $applozic('#mck-group-info-btn, #mck-group-info-tab .mck-box-title').html(MCK_LABELS['group.info.title']).attr('title', MCK_LABELS['group.info.title']);
        $applozic('#mck-gi-overlay-label').html(MCK_LABELS['change.group.icon']);
        $applozic('#mck-group-member-title').html(MCK_LABELS['members.title']).attr('title', MCK_LABELS['members.title']);
        $applozic('#mck-group-add-member .blk-lg-9, #mck-gm-search-box .mck-box-title').html(MCK_LABELS['add.members.title']).attr('title', MCK_LABELS['add.members.title']);
        $applozic('#mck-btn-group-update').html(MCK_LABELS['group.info.update']).attr('title', MCK_LABELS['group.info.update']);
        $applozic('#mck-leave-group-btn, #mck-btn-group-exit').html(MCK_LABELS['exit.group']).attr('title', MCK_LABELS['exit.group']);
        $applozic('#mck-btn-leave-group, #mck-btn-group-exit').html(MCK_LABELS['exit.group']).attr('title', MCK_LABELS['exit.group']);
        $applozic('#mck-typing-label').html(MCK_LABELS['typing']);
        $applozic('#mck-btn-clear-messages').html(MCK_LABELS['clear.messages']).attr('title', MCK_LABELS['clear.messages']);
        $applozic('#mck-block-button').html(MCK_LABELS['block.user']).attr('title', MCK_LABELS['block.user']);
        $applozic('#mck-loc-box .mck-box-title, #mck-share-loc-label').html(MCK_LABELS['location.share.title']).attr('title', MCK_LABELS['location.share.title']);
        $applozic('#mck-btn-loc').attr('title', MCK_LABELS['location.share.title']);
        $applozic('#mck-file-up-label').html(MCK_LABELS['file.attachment']);
        $applozic('#mck-file-up').attr('title', MCK_LABELS['file.attachment']);
        $applozic('.mck-file-attach-label').attr('title', MCK_LABELS['file.attach.title']);
        $applozic('#mck-my-loc').html(MCK_LABELS['my.location']).attr('title', MCK_LABELS['my.location']);
        $applozic('#mck-btn-close-loc-box').html(MCK_LABELS['close']).attr('title', MCK_LABELS['close']);
        $applozic('#mck-loc-submit').html(MCK_LABELS['send']).attr('title', MCK_LABELS['send']);
        $applozic('#mck-msg-sbmt').attr('title', MCK_LABELS['send.message'])
        $applozic('#mck-btn-smiley').attr('title', MCK_LABELS['smiley']);
        $applozic('#mck-group-name-save').attr('title', MCK_LABELS['save']);
        $applozic('#mck-btn-group-icon-save').attr('title', MCK_LABELS['save']);
        $applozic('#mck-group-name-edit').attr('title', MCK_LABELS['edit']);
        $applozic('#mck-contact-search-input').attr('title', MCK_LABELS['charsNotAllowedMessage']);
    };
};
   