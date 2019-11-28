OPENEDU_EXCEL_DEFINITION = [
    {
        'func': 'add_format',
        'kwargs': {
            'key': 'top_header',
            'format': {
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'vcenter',
                'fg_color': 'yellow'
            }
        }
    },
    {
        'func': 'add_format',
        'kwargs': {
            'key': 'header',
            'format': {
                'border': 1,
                'bg_color': '#C6EFCE',
                'bold': True,
                'text_wrap': True,
                'valign': 'vcenter',
                'indent': 1,
            }
        }
    },
    {
        'func': 'add_format',
        'kwargs': {
            'key': 'header_required',
            'format': {
                'border': 1,
                'bg_color': '#226b30',
                'bold': True,
                'text_wrap': True,
                'valign': 'vcenter',
                'indent': 1,
            }
        }
    },
    {
        'func': 'add_format',
        'kwargs': {
            'key': 'locked',
            'format': {
                'locked': True
            }
        }
    },
    {
        'func': 'add_format',
        'kwargs': {
            'key': 'unlocked',
            'format': {
                'locked': False
            }
        }
    },
    {
        'func': 'add_format',
        'kwargs': {
            'key': 'currency',
            'format': {
            },
            'num_format': 'R 0'
        }
    },
    {
        'group_name': 'General',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Qualification ID',
                    'key': 'qualification__id',
                    'validations': {
                        'excel': {
                            'validate': 'integer',
                            'criteria': '>=',
                            'value': 0,
                            'input_title': 'ID',
                            'input_message': 'Cant touch this'  # noqa
                        }
                    },
                    'format': 'locked'
                },
                {
                    'name': 'Campus name',
                    'key': 'campus__name',
                    'validations': {
                        'list_source_func': 'get_campus_list',
                    },
                    'format': 'locked'
                },
                {
                    'name': 'SAQA Qualification name',
                    'key': 'saqa_qualification__name',
                    'validations': {
                        'excel': {
                            'validate': 'length',
                            'criteria': 'between',
                            'minimum': 0,
                            'maximum': 255,
                            'input_title': 'SAQA qualification name',
                            'input_message': 'Maximum of 255 characters.'
                        }
                    },
                    'format': 'unlocked'
                },
                {
                    'name': 'SAQA Qualification ID',
                    'key': 'saqa_qualification__saqa_id',
                    'validations': {
                        'excel': {
                            'validate': 'integer',
                            'criteria': '>=',
                            'value': 0,
                            'input_title': 'SAQA id',
                            'input_message': 'If accredited, enter the correct SAQA id\nIf not, enter 0.' # noqa
                        }
                    },
                    'format': 'unlocked'
                },
                {
                    'name': 'Is it still active?',
                    'key': 'qualification__deleted',
                    'validations': {
                        'list_source_func': 'get_yes_no_list',
                    },
                    'format': 'locked'
                },
                {
                    'name': 'Short description',
                    'key': 'qualification__short_description',
                    'validations': {
                        'excel': {
                            'validate': 'length',
                            'criteria': 'between',
                            'minimum': 0,
                            'maximum': 250,
                            'input_title': 'Short description',
                            'input_message': 'Maximum of 250 characters'
                        }
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Long description',
                    'key': 'qualification__long_description',
                    'validations': {
                        'excel': {
                            'validate': 'length',
                            'criteria': 'between',
                            'minimum': 0,
                            'maximum': 500,
                            'input_title': 'Long description',
                            'input_message': 'Maximum of 500 characters'
                        }
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Distance Learning',
                    'key': 'qualification__distance_learning',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Full time / Part time',
                    'key': 'qualification__full_part_time',
                    'validations': {
                        'list_source_func': 'get_full_part_time_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Web page',
                    'key': 'qualification__webpage',
                    'validations': {
                        'excel': {
                            'validate': 'any',
                            'input_title': 'Qualification webpage',
                            'input_message': 'Must be an internet link (http://)'  # noqa
                        }
                    }
                }
            ],

        }
    },
    {
        'group_name': 'Duration',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Duration',
                    'key': 'qualification__duration',
                    'validations': {
                        'excel': {
                            'validate': 'integer',
                            'criteria': '>=',
                            'value': 1,
                            'input_title': 'Duration',
                            'input_message': 'e.g: 6 months / 2 years\nChoose month or year at the next column.' # noqa
                        }
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Duration - ',
                    'key': 'qualification__time_repr',
                    'validations': {
                        'list_source_func': 'get_qualification_time_repr_list'
                    },
                    'required': True
                }
            ]
        }
    },
    {
        'group_name': 'Cost',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Total cost',
                    'key': 'qualification__total_cost',
                    'validations': {
                        'excel': {
                            'validate': 'integer',
                            'criteria': '>=',
                            'value': 1,
                            'input_title': 'Cost',
                            'input_message': 'Average cost of the full qualification.' # noqa
                        }
                    },
                    'format': 'currency',
                    'required': True
                },
                {
                    'name': 'Total Cost comment',
                    'key': 'qualification__total_cost_comment',
                    'validations': {
                        'excel': {
                            'validate': 'length',
                            'criteria': 'between',
                            'minimum': 0,
                            'maximum': 255,
                            'input_title': 'Cost comment',
                            'input_message': 'Any comments regarding the cost and payment options of this qualification should be filled in here.' # noqa
                        }
                    },
                    'format': 'unlocked',
                    'required': True
                }
            ]
        }
    },
    {
        'group_name': 'Job Prospect',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Preparation for critical skill?',
                    'key': 'qualification__critical_skill',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Preparation for green job?',
                    'key': 'qualification__green_occupation',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Preparation for high demand job?',
                    'key': 'qualification__high_demand_occupation',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                }

            ]
        }
    },
    {
        'group_name': 'Qualification Requirements',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Required entrance qualification',
                    'key': 'requirement__min_nqf_level',
                    'validations': {
                        'list_source_func': 'get_required_entrance_qualification_list'  # noqa
                    },
                    'format': 'unlocked'
                },
                {
                    'name': 'Is there an interview?',
                    'key': 'requirement__interview',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Does it require a portfolio?',
                    'key': 'requirement__portfolio',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Portfolio requirements',
                    'key': 'requirement__portfolio_comment',
                    'validations': {},
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Does it involve any other assessment?',
                    'key': 'requirement__assessment',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                },
                {
                    'name': 'Assessment requirements',
                    'key': 'requirement__assessment_comment',
                    'validations': {},
                    'format': 'unlocked',
                    'required': True
                },

            ]
        }
    },
    {
        'group_name': 'APS',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Does it require an APS score?',
                    'key': 'requirement__require_aps_score',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'format': 'unlocked',
                    'required': True
                }
            ]
        }
    },
    {
        'group_name': 'APS for groups',
        'func': 'add_group_column',
        'kwargs': {
            'repeat_func': 'get_number_of_people_groups',
            'columns': [
                {
                    'name_func': 'get_name_of_people_group',
                    'key': 'admission_point_score__value',
                    'validations': {
                        'excel': {
                            'validate': 'integer',
                            'criteria': '>=',
                            'value': 1,
                            'input_title': 'APS score',
                            'input_message': '' # noqa
                        }
                    },
                }
            ]
        }
    },
    {
        'group_name': '',
        'func': 'add_group_column',
        'kwargs': {
            'columns': [
                {
                    'name': 'Does it require certain subjects?',
                    'key': 'requirement__require_certain_subjects',
                    'validations': {
                        'list_source_func': 'get_yes_no_list'
                    },
                    'required': True
                }
            ]
        }
    },
    {
        'group_name': 'Required subjects and scores',
        'func': 'add_group_column',
        'kwargs': {
            'repeat': 5,
            'columns': [
                {
                    'name': 'Subject',
                    'key': 'qualification_entrance_requirement_subject__subject',  # noqa
                    'validations': {
                        'list_source_func': 'get_subjects_list'
                    },
                    'format': 'unlocked'
                },
                {
                    'name': 'Score',
                    'key': 'qualification_entrance_requirement_subject__minimum_score',  # noqa
                    'validations': {
                        'excel': {
                            'validate': 'integer',
                            'criteria': 'between',
                            'minimum': 1,
                            'maximum': 100,
                            'input_title': 'Score',
                            'input_message': 'Between 1 and 100.'
                        }
                    },
                    'format': 'unlocked'
                }
            ]
        }
    },
    {
        'group_name': 'Associated occupations',
        'func': 'add_group_column',
        'kwargs': {
            'repeat': 5,
            'columns': [
                {
                    'name': 'Occupations',
                    'key': 'occupation__name',
                    'validations': {
                        'list_source_func': 'get_occupations_list'
                    },
                    'format': 'unlocked'
                }
            ]
        }
    },
    {
        'group_name': 'Associated interests',
        'func': 'add_group_column',
        'kwargs': {
            'repeat': 3,
            'columns': [
                {
                    'name': 'Interests',
                    'key': 'interest__name',
                    'validations': {
                        'list_source_func': 'get_interests_list'
                    },
                    'format': 'unlocked'
                }
            ]
        }
    }
]
