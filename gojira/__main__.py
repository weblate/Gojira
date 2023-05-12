# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2023 Hitalo M. <https://github.com/HitaloM>

import asyncio

from gojira import bot, dp, i18n
from gojira.handlers import anime, language, manga, pm_menu, users, view
from gojira.middlewares.acl import ACLMiddleware
from gojira.middlewares.i18n import MyI18nMiddleware
from gojira.utils.command_list import set_ui_commands


async def main():
    dp.message.middleware(ACLMiddleware())
    dp.message.middleware(MyI18nMiddleware(i18n=i18n))
    dp.callback_query.middleware(ACLMiddleware())
    dp.callback_query.middleware(MyI18nMiddleware(i18n=i18n))
    dp.inline_query.middleware(ACLMiddleware())
    dp.inline_query.middleware(MyI18nMiddleware(i18n=i18n))

    dp.include_routers(
        pm_menu.router,
        view.router,
        language.router,
        anime.start.router,
        anime.view.router,
        anime.upcoming.router,
        anime.popular.router,
        anime.categories.router,
        anime.scan.router,
        anime.inline.router,
        manga.view.router,
        manga.start.router,
        manga.upcoming.router,
        manga.popular.router,
        manga.categories.router,
        manga.inline.router,
        users.router,
    )

    await set_ui_commands(bot, i18n)

    useful_updates = dp.resolve_used_update_types()

    await dp.start_polling(bot, allowed_updates=useful_updates)


if __name__ == "__main__":
    asyncio.run(main())
