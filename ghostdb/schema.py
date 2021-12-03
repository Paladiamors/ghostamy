# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Index, Integer, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .mixins import UserMixin

Base = declarative_base()
metadata = Base.metadata


class Action(Base):
    __tablename__ = 'actions'

    id = Column(String(24), primary_key=True)
    resource_id = Column(String(24))
    resource_type = Column(String(50), nullable=False)
    actor_id = Column(String(24), nullable=False)
    actor_type = Column(String(50), nullable=False)
    event = Column(String(50), nullable=False)
    context = Column(Text)
    created_at = Column(DateTime, nullable=False)


class ApiKey(Base):
    __tablename__ = 'api_keys'

    id = Column(String(24), primary_key=True)
    type = Column(String(50), nullable=False)
    secret = Column(String(191), nullable=False, unique=True)
    role_id = Column(String(24))
    integration_id = Column(String(24))
    user_id = Column(String(24))
    last_seen_at = Column(DateTime)
    last_seen_version = Column(String(50))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Benefit(Base):
    __tablename__ = 'benefits'

    id = Column(String(24), primary_key=True)
    name = Column(String(191), nullable=False)
    slug = Column(String(191), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)


class Brute(Base):
    __tablename__ = 'brute'

    key = Column(String(191), primary_key=True)
    firstRequest = Column(BigInteger, nullable=False)
    lastRequest = Column(BigInteger, nullable=False)
    lifetime = Column(BigInteger, nullable=False)
    count = Column(Integer, nullable=False)


class CustomThemeSetting(Base):
    __tablename__ = 'custom_theme_settings'

    id = Column(String(24), primary_key=True)
    theme = Column(String(191), nullable=False)
    key = Column(String(191), nullable=False)
    type = Column(String(50), nullable=False)
    value = Column(Text)


class Email(Base):
    __tablename__ = 'emails'

    id = Column(String(24), primary_key=True)
    post_id = Column(String(24), nullable=False, unique=True)
    uuid = Column(String(36), nullable=False)
    status = Column(String(50), nullable=False, server_default=text("'pending'"))
    recipient_filter = Column(String(50), nullable=False, server_default=text("'status:-free'"))
    error = Column(String(2000))
    error_data = Column(LONGTEXT)
    email_count = Column(INTEGER, nullable=False, server_default=text("'0'"))
    delivered_count = Column(INTEGER, nullable=False, server_default=text("'0'"))
    opened_count = Column(INTEGER, nullable=False, server_default=text("'0'"))
    failed_count = Column(INTEGER, nullable=False, server_default=text("'0'"))
    subject = Column(String(300))
    _from = Column('from', String(2000))
    reply_to = Column(String(2000))
    html = Column(LONGTEXT)
    plaintext = Column(LONGTEXT)
    track_opens = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    submitted_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Integration(Base):
    __tablename__ = 'integrations'

    id = Column(String(24), primary_key=True)
    type = Column(String(50), nullable=False, server_default=text("'custom'"))
    name = Column(String(191), nullable=False)
    slug = Column(String(191), nullable=False, unique=True)
    icon_image = Column(String(2000))
    description = Column(String(2000))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Invite(Base):
    __tablename__ = 'invites'

    id = Column(String(24), primary_key=True)
    role_id = Column(String(24), nullable=False)
    status = Column(String(50), nullable=False, server_default=text("'pending'"))
    token = Column(String(191), nullable=False, unique=True)
    email = Column(String(191), nullable=False, unique=True)
    expires = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Label(Base):
    __tablename__ = 'labels'

    id = Column(String(24), primary_key=True)
    name = Column(String(191), nullable=False, unique=True)
    slug = Column(String(191), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Member(Base):
    __tablename__ = 'members'

    id = Column(String(24), primary_key=True)
    uuid = Column(String(36), unique=True)
    email = Column(String(191), nullable=False, unique=True)
    status = Column(String(50), nullable=False, server_default=text("'free'"))
    name = Column(String(191))
    note = Column(String(2000))
    geolocation = Column(String(2000))
    subscribed = Column(TINYINT(1), server_default=text("'1'"))
    email_count = Column(INTEGER, nullable=False, server_default=text("'0'"))
    email_opened_count = Column(INTEGER, nullable=False, server_default=text("'0'"))
    email_open_rate = Column(INTEGER, index=True)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Migration(Base):
    __tablename__ = 'migrations'
    __table_args__ = (
        Index('migrations_name_version_unique', 'name', 'version', unique=True),
    )

    id = Column(INTEGER, primary_key=True)
    name = Column(String(120), nullable=False)
    version = Column(String(70), nullable=False)
    currentVersion = Column(String(255))


class MigrationsLock(Base):
    __tablename__ = 'migrations_lock'

    lock_key = Column(String(191), primary_key=True)
    locked = Column(TINYINT(1), server_default=text("'0'"))
    acquired_at = Column(DateTime)
    released_at = Column(DateTime)


class MobiledocRevision(Base):
    __tablename__ = 'mobiledoc_revisions'

    id = Column(String(24), primary_key=True)
    post_id = Column(String(24), nullable=False, index=True)
    mobiledoc = Column(LONGTEXT)
    created_at_ts = Column(BigInteger, nullable=False)
    created_at = Column(DateTime, nullable=False)


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(String(24), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    object_type = Column(String(50), nullable=False)
    action_type = Column(String(50), nullable=False)
    object_id = Column(String(24))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class PermissionsRole(Base):
    __tablename__ = 'permissions_roles'

    id = Column(String(24), primary_key=True)
    role_id = Column(String(24), nullable=False)
    permission_id = Column(String(24), nullable=False)


class PermissionsUser(Base):
    __tablename__ = 'permissions_users'

    id = Column(String(24), primary_key=True)
    user_id = Column(String(24), nullable=False)
    permission_id = Column(String(24), nullable=False)


class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = (
        Index('posts_slug_type_unique', 'slug', 'type', unique=True),
    )

    id = Column(String(24), primary_key=True)
    uuid = Column(String(36), nullable=False)
    title = Column(String(2000), nullable=False)
    slug = Column(String(191), nullable=False)
    mobiledoc = Column(LONGTEXT)
    html = Column(LONGTEXT)
    comment_id = Column(String(50))
    plaintext = Column(LONGTEXT)
    feature_image = Column(String(2000))
    featured = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    type = Column(String(50), nullable=False, server_default=text("'post'"))
    status = Column(String(50), nullable=False, server_default=text("'draft'"))
    locale = Column(String(6))
    visibility = Column(String(50), nullable=False, server_default=text("'public'"))
    email_recipient_filter = Column(String(50), nullable=False, server_default=text("'none'"))
    author_id = Column(String(24), nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))
    published_at = Column(DateTime)
    published_by = Column(String(24))
    custom_excerpt = Column(String(2000))
    codeinjection_head = Column(Text)
    codeinjection_foot = Column(Text)
    custom_template = Column(String(100))
    canonical_url = Column(Text)


class Product(Base):
    __tablename__ = 'products'

    id = Column(String(24), primary_key=True)
    name = Column(String(191), nullable=False)
    slug = Column(String(191), nullable=False, unique=True)
    monthly_price_id = Column(String(24))
    yearly_price_id = Column(String(24))
    description = Column(String(191))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)


class Role(Base):
    __tablename__ = 'roles'

    id = Column(String(24), primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(2000))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class RolesUser(Base):
    __tablename__ = 'roles_users'

    id = Column(String(24), primary_key=True)
    role_id = Column(String(24), nullable=False)
    user_id = Column(String(24), nullable=False)


class Session(Base):
    __tablename__ = 'sessions'

    id = Column(String(24), primary_key=True)
    session_id = Column(String(32), nullable=False, unique=True)
    user_id = Column(String(24), nullable=False)
    session_data = Column(String(2000), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)


class Setting(Base):
    __tablename__ = 'settings'

    id = Column(String(24), primary_key=True)
    group = Column(String(50), nullable=False, server_default=text("'core'"))
    key = Column(String(50), nullable=False, unique=True)
    value = Column(Text)
    type = Column(String(50), nullable=False)
    flags = Column(String(50))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Snippet(Base):
    __tablename__ = 'snippets'

    id = Column(String(24), primary_key=True)
    name = Column(String(191), nullable=False, unique=True)
    mobiledoc = Column(LONGTEXT, nullable=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(String(24), primary_key=True)
    name = Column(String(191), nullable=False)
    slug = Column(String(191), nullable=False, unique=True)
    description = Column(Text)
    feature_image = Column(String(2000))
    parent_id = Column(String(191))
    visibility = Column(String(50), nullable=False, server_default=text("'public'"))
    og_image = Column(String(2000))
    og_title = Column(String(300))
    og_description = Column(String(500))
    twitter_image = Column(String(2000))
    twitter_title = Column(String(300))
    twitter_description = Column(String(500))
    meta_title = Column(String(2000))
    meta_description = Column(String(2000))
    codeinjection_head = Column(Text)
    codeinjection_foot = Column(Text)
    canonical_url = Column(String(2000))
    accent_color = Column(String(50))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class TempMemberAnalyticEvent(Base):
    __tablename__ = 'temp_member_analytic_events'

    id = Column(String(24), primary_key=True)
    event_name = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    member_id = Column(String(24), nullable=False)
    member_status = Column(String(50), nullable=False)
    entry_id = Column(String(24))
    source_url = Column(String(2000))
    metadata_ = Column('metadata', String(191))


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(String(24), primary_key=True)
    token = Column(String(32), nullable=False, index=True)
    data = Column(String(2000))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(String(24), primary_key=True)
    name = Column(String(191), nullable=False)
    slug = Column(String(191), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    email = Column(String(191), nullable=False, unique=True)
    profile_image = Column(String(2000))
    cover_image = Column(String(2000))
    bio = Column(Text)
    website = Column(String(2000))
    location = Column(Text)
    facebook = Column(String(2000))
    twitter = Column(String(2000))
    accessibility = Column(Text)
    status = Column(String(50), nullable=False, server_default=text("'active'"))
    locale = Column(String(6))
    visibility = Column(String(50), nullable=False, server_default=text("'public'"))
    meta_title = Column(String(2000))
    meta_description = Column(String(2000))
    tour = Column(Text)
    last_seen = Column(DateTime)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))


class EmailBatch(Base):
    __tablename__ = 'email_batches'

    id = Column(String(24), primary_key=True)
    email_id = Column(ForeignKey('emails.id'), nullable=False, index=True)
    provider_id = Column(String(255))
    status = Column(String(50), nullable=False, server_default=text("'pending'"))
    member_segment = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    email = relationship('Email')


class MembersEmailChangeEvent(Base):
    __tablename__ = 'members_email_change_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    to_email = Column(String(191), nullable=False)
    from_email = Column(String(191), nullable=False)
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')


class MembersLabel(Base):
    __tablename__ = 'members_labels'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    label_id = Column(ForeignKey('labels.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(INTEGER, nullable=False, server_default=text("'0'"))

    label = relationship('Label')
    member = relationship('Member')


class MembersLoginEvent(Base):
    __tablename__ = 'members_login_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')


class MembersPaidSubscriptionEvent(Base):
    __tablename__ = 'members_paid_subscription_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    from_plan = Column(String(255))
    to_plan = Column(String(255))
    currency = Column(String(191), nullable=False)
    source = Column(String(50), nullable=False)
    mrr_delta = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')


class MembersPaymentEvent(Base):
    __tablename__ = 'members_payment_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    currency = Column(String(191), nullable=False)
    source = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')


class MembersProductEvent(Base):
    __tablename__ = 'members_product_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('products.id'), nullable=False, index=True)
    action = Column(String(50))
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')
    product = relationship('Product')


class MembersProduct(Base):
    __tablename__ = 'members_products'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(INTEGER, nullable=False, server_default=text("'0'"))

    member = relationship('Member')
    product = relationship('Product')


class MembersStatusEvent(Base):
    __tablename__ = 'members_status_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    from_status = Column(String(50))
    to_status = Column(String(50))
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')


class MembersStripeCustomer(Base):
    __tablename__ = 'members_stripe_customers'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    customer_id = Column(String(255), nullable=False, unique=True)
    name = Column(String(191))
    email = Column(String(191))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))

    member = relationship('Member')


class MembersSubscribeEvent(Base):
    __tablename__ = 'members_subscribe_events'

    id = Column(String(24), primary_key=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    subscribed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    created_at = Column(DateTime, nullable=False)
    source = Column(String(50))

    member = relationship('Member')


class Oauth(Base):
    __tablename__ = 'oauth'

    id = Column(String(24), primary_key=True)
    provider = Column(String(50), nullable=False)
    provider_id = Column(String(191), nullable=False)
    access_token = Column(Text)
    refresh_token = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)

    user = relationship('User')


class Offer(Base):
    __tablename__ = 'offers'

    id = Column(String(24), primary_key=True)
    active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    name = Column(String(191), nullable=False, unique=True)
    code = Column(String(191), nullable=False, unique=True)
    product_id = Column(ForeignKey('products.id'), nullable=False, index=True)
    stripe_coupon_id = Column(String(255), unique=True)
    interval = Column(String(50), nullable=False)
    currency = Column(String(50))
    discount_type = Column(String(50), nullable=False)
    discount_amount = Column(Integer, nullable=False)
    duration = Column(String(50), nullable=False)
    duration_in_months = Column(Integer)
    portal_title = Column(String(191))
    portal_description = Column(String(2000))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    product = relationship('Product')


class PostsAuthor(Base):
    __tablename__ = 'posts_authors'

    id = Column(String(24), primary_key=True)
    post_id = Column(ForeignKey('posts.id'), nullable=False, index=True)
    author_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    sort_order = Column(INTEGER, nullable=False, server_default=text("'0'"))

    author = relationship('User')
    post = relationship('Post')


class PostsMeta(Base):
    __tablename__ = 'posts_meta'

    id = Column(String(24), primary_key=True)
    post_id = Column(ForeignKey('posts.id'), nullable=False, unique=True)
    og_image = Column(String(2000))
    og_title = Column(String(300))
    og_description = Column(String(500))
    twitter_image = Column(String(2000))
    twitter_title = Column(String(300))
    twitter_description = Column(String(500))
    meta_title = Column(String(2000))
    meta_description = Column(String(2000))
    email_subject = Column(String(300))
    frontmatter = Column(Text)
    feature_image_alt = Column(String(191))
    feature_image_caption = Column(Text)
    email_only = Column(TINYINT(1), nullable=False, server_default=text("'0'"))

    post = relationship('Post')


class PostsTag(Base):
    __tablename__ = 'posts_tags'

    id = Column(String(24), primary_key=True)
    post_id = Column(ForeignKey('posts.id'), nullable=False, index=True)
    tag_id = Column(ForeignKey('tags.id'), nullable=False, index=True)
    sort_order = Column(INTEGER, nullable=False, server_default=text("'0'"))

    post = relationship('Post')
    tag = relationship('Tag')


class ProductsBenefit(Base):
    __tablename__ = 'products_benefits'

    id = Column(String(24), primary_key=True)
    product_id = Column(ForeignKey('products.id', ondelete='CASCADE'), nullable=False, index=True)
    benefit_id = Column(ForeignKey('benefits.id', ondelete='CASCADE'), nullable=False, index=True)
    sort_order = Column(INTEGER, nullable=False, server_default=text("'0'"))

    benefit = relationship('Benefit')
    product = relationship('Product')


class StripeProduct(Base):
    __tablename__ = 'stripe_products'

    id = Column(String(24), primary_key=True)
    product_id = Column(ForeignKey('products.id'), nullable=False, index=True)
    stripe_product_id = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    product = relationship('Product')


class Webhook(Base):
    __tablename__ = 'webhooks'

    id = Column(String(24), primary_key=True)
    event = Column(String(50), nullable=False)
    target_url = Column(String(2000), nullable=False)
    name = Column(String(191))
    secret = Column(String(191))
    api_version = Column(String(50), nullable=False, server_default=text("'v2'"))
    integration_id = Column(ForeignKey('integrations.id', ondelete='CASCADE'), nullable=False, index=True)
    status = Column(String(50), nullable=False, server_default=text("'available'"))
    last_triggered_at = Column(DateTime)
    last_triggered_status = Column(String(50))
    last_triggered_error = Column(String(50))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))

    integration = relationship('Integration')


class EmailRecipient(Base):
    __tablename__ = 'email_recipients'
    __table_args__ = (
        Index('email_recipients_email_id_member_email_index', 'email_id', 'member_email'),
    )

    id = Column(String(24), primary_key=True)
    email_id = Column(ForeignKey('emails.id'), nullable=False)
    member_id = Column(String(24), nullable=False, index=True)
    batch_id = Column(ForeignKey('email_batches.id'), nullable=False, index=True)
    processed_at = Column(DateTime)
    delivered_at = Column(DateTime, index=True)
    opened_at = Column(DateTime, index=True)
    failed_at = Column(DateTime, index=True)
    member_uuid = Column(String(36), nullable=False)
    member_email = Column(String(191), nullable=False)
    member_name = Column(String(191))

    batch = relationship('EmailBatch')
    email = relationship('Email')


class MembersStripeCustomersSubscription(Base):
    __tablename__ = 'members_stripe_customers_subscriptions'

    id = Column(String(24), primary_key=True)
    customer_id = Column(ForeignKey('members_stripe_customers.customer_id', ondelete='CASCADE'), nullable=False, index=True)
    subscription_id = Column(String(255), nullable=False, unique=True)
    stripe_price_id = Column(String(255), nullable=False, index=True, server_default=text("''"))
    status = Column(String(50), nullable=False)
    cancel_at_period_end = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    cancellation_reason = Column(String(500))
    current_period_end = Column(DateTime, nullable=False)
    start_date = Column(DateTime, nullable=False)
    default_payment_card_last4 = Column(String(4))
    created_at = Column(DateTime, nullable=False)
    created_by = Column(String(24), nullable=False)
    updated_at = Column(DateTime)
    updated_by = Column(String(24))
    plan_id = Column(String(255), nullable=False)
    plan_nickname = Column(String(50), nullable=False)
    plan_interval = Column(String(50), nullable=False)
    plan_amount = Column(Integer, nullable=False)
    plan_currency = Column(String(191), nullable=False)

    customer = relationship('MembersStripeCustomer')


class StripePrice(Base):
    __tablename__ = 'stripe_prices'

    id = Column(String(24), primary_key=True)
    stripe_price_id = Column(String(255), nullable=False, unique=True)
    stripe_product_id = Column(ForeignKey('stripe_products.stripe_product_id'), nullable=False, index=True)
    active = Column(TINYINT(1), nullable=False)
    nickname = Column(String(50))
    currency = Column(String(191), nullable=False)
    amount = Column(Integer, nullable=False)
    type = Column(String(50), nullable=False, server_default=text("'recurring'"))
    interval = Column(String(50))
    description = Column(String(191))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)

    stripe_product = relationship('StripeProduct')


class OfferRedemption(Base):
    __tablename__ = 'offer_redemptions'

    id = Column(String(24), primary_key=True)
    offer_id = Column(ForeignKey('offers.id', ondelete='CASCADE'), nullable=False, index=True)
    member_id = Column(ForeignKey('members.id', ondelete='CASCADE'), nullable=False, index=True)
    subscription_id = Column(ForeignKey('members_stripe_customers_subscriptions.id', ondelete='CASCADE'), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False)

    member = relationship('Member')
    offer = relationship('Offer')
    subscription = relationship('MembersStripeCustomersSubscription')
