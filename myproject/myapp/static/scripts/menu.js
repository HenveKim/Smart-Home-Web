let menuOptions = [{
    text: "导入数据列表",
    subs: [
        {
            text: "全部数据",
            attributes: {
                "data-url": "",
            },
            subs: [
                {
                    text: "消费金额",
                    attributes: {
                        "data-url": "",
                    }
                }, {
                    text: "放款金额",
                    attributes: {
                        "data-url": "",
                    }
                }, {
                    text: "返佣金额",
                    attributes: {
                        "data-url": "",
                    }
                }, {
                    text: "导入数据",
                    attributes: {
                        "data-url": "",
                    }
                }, {
                    text: "查看",
                    attributes: {
                        "data-url": "",
                    }
                }, {
                    text: "编辑",
                    attributes: {
                        "data-url": "",
                    }
                }
            ]
        }, {
            text: "消费金额",
            attributes: {
                "data-url": "",
            }
        }, {
            text: "放款金额",
            attributes: {
                "data-url": "",
            }
        }, {
            text: "返佣金额",
            attributes: {
                "data-url": "",
            }
        }, {
            text: "导入数据",
            attributes: {
                "data-url": "",
            }
        }, {
            text: "查看",
            attributes: {
                "data-url": "",
            }
        }, {
            text: "编辑",
            attributes: {
                "data-url": "",
            }
        }
    ]
}, {
    text: "异常数据列表",
    subs: []
}, {
    text: "数据修正",
    subs: []
}, {
    text: "修正审核-客服经理",
    subs: []
}, {
    text: "修正审核-财务",
    subs: []
}, {
    text: "导入日志",
    subs: []
}]
 
window.onload = function () {
    new WenMenu({
        ele: document.querySelector('.readme-menu-box'), // 菜单插入的位置
        menus: menuOptions,
        event: function (e) { }, // 菜单最底端点击事件触发
        attributes: {}, // 最外层ul属性设置
        menuHeight: 35, // 每个菜单项的高度
        autoCollapse: true, // 是否自动收起无活动菜单
    })
};